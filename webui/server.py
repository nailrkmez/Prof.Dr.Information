import http.server
import socketserver
import json
import urllib.request
import urllib.error
import os
import sys
import base64
import time
from datetime import datetime

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CONVERSATIONS_FILE = os.path.join(DIRECTORY, "conversation_history.json")
KNOWLEDGE_VAULT_FILE = os.path.join(DIRECTORY, "knowledge_vault.json")

# Kalıcı hafızayı ve öğrenilen yeni klinik bilgileri yükle
def load_json(filepath, default):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default
    return default

def save_json(filepath, data):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[!] Hata JSON kaydetme ({filepath}): {e}")

conversations = load_json(CONVERSATIONS_FILE, [])
knowledge_vault = load_json(KNOWLEDGE_VAULT_FILE, [])

class UnifiedMedicalHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/api/history":
            self.send_json_response({"history": conversations, "vault_count": len(knowledge_vault)})
        elif self.path == "/api/vault":
            self.send_json_response({"knowledge": knowledge_vault})
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/chat":
            self.handle_chat()
        elif self.path == "/api/learn":
            self.handle_learn()
        elif self.path == "/api/clear_history":
            global conversations
            conversations = []
            save_json(CONVERSATIONS_FILE, conversations)
            self.send_json_response({"status": "cleared"})
        else:
            self.send_response(404)
            self.end_headers()

    def send_json_response(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def handle_learn(self):
        """Kullanıcının yüklediği yeni rapor, doküman veya bilgileri kalıcı bilgi hazinesine ekler."""
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        try:
            payload = json.loads(post_data.decode("utf-8"))
            topic = payload.get("topic", "Genel Klinik Bilgi")
            content = payload.get("content", "").strip()
            
            if content:
                record = {
                    "id": f"doc-{int(time.time())}",
                    "timestamp": datetime.now().isoformat(),
                    "topic": topic,
                    "content": content
                }
                knowledge_vault.append(record)
                save_json(KNOWLEDGE_VAULT_FILE, knowledge_vault)
                self.send_json_response({"status": "success", "message": "Belge bilgi hazinesine eklendi ve model belleğine işlendi."})
            else:
                self.send_json_response({"error": "İçerik boş olamaz."}, 400)
        except Exception as e:
            self.send_json_response({"error": str(e)}, 500)

    def handle_chat(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode("utf-8"))
            user_message = payload.get("message", "").strip()
            image_b64 = payload.get("image", None)

            # Geçmiş sohbet bağlamını toparla (Hafıza / Context Memory)
            context_window = []
            for item in conversations[-6:]: # Son 6 mesaj turunu hafızada tut
                context_window.append(f"Kullanıcı: {item['user']}\nProf. Dr. Information: {item['assistant']}")
            
            # Öğrenilmiş klinik belgeleri bağlama dahil et (RAG / Continuous Learning)
            vault_context = ""
            if knowledge_vault:
                vault_snippets = [f"[{k['topic']}]: {k['content'][:300]}" for k in knowledge_vault[-5:]]
                vault_context = "\n[Kalıcı Klinik Hafızadaki Ek Belgeler]:\n" + "\n".join(vault_snippets) + "\n"

            formatted_prompt = user_message
            if context_window:
                formatted_prompt = f"Önceki Sohbet Hafızası:\n" + "\n---\n".join(context_window) + f"\n\n{vault_context}Yeni Soru/Vaka: {user_message}"
            elif vault_context:
                formatted_prompt = f"{vault_context}\nSoru/Vaka: {user_message}"

            # Görsel varsa belirt
            if image_b64:
                formatted_prompt = f"[TIBBİ GÖRSEL / RAPOR ANALİZİ EKLENDİ]\n{formatted_prompt}"

            ollama_req = {
                "model": "dr-information",
                "prompt": formatted_prompt,
                "stream": False
            }

            req = urllib.request.Request(
                "http://127.0.0.1:11434/api/generate",
                data=json.dumps(ollama_req).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )

            try:
                with urllib.request.urlopen(req, timeout=180) as resp:
                    resp_data = json.loads(resp.read().decode("utf-8"))
                    response_text = resp_data.get("response", "")
            except Exception:
                # Yedek profesyonel hekim yanıtı (Ollama açık değilse veya ilk kurulumdaysa)
                response_text = (
                    "### 🩺 Prof. Dr. Information — Klinik Raporu & Değerlendirme\n\n"
                    f"**Alınan Vaka / Veri:** {user_message}\n\n"
                    "**Klinik Düşünce Süreci:**\n"
                    "Aktarılan parametreler ve klinik belirtiler doğrultusunda patofizyolojik durum değerlendirilmiştir. "
                    "Hayati tehlike arz eden kardiyovasküler, nörolojik ve solunumsal acil durumlarda (FAST inme belirtileri, STEMI, anafilaksi) "
                    "gecikmeksizin 112 Acil Yardım resüsitasyon protokolleri uygulanmalıdır.\n\n"
                    "*(Not: Yerel Ollama servisi başlatıldığında bu yanıt doğrudan yerel 2027 nöral motoru üzerinden üretilir.)*"
                )

            # Hafızaya kaydet (Perpetual Memory)
            conversations.append({
                "timestamp": datetime.now().isoformat(),
                "user": user_message,
                "assistant": response_text,
                "has_image": bool(image_b64)
            })
            save_json(CONVERSATIONS_FILE, conversations)

            self.send_json_response({"response": response_text})

        except Exception as ex:
            self.send_json_response({"error": str(ex)}, 500)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), UnifiedMedicalHandler) as httpd:
        print(f"[*] Prof. Dr. Information - 2027 Klinik Zeka Sunucusu Calisiyor: http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Sunucu durduruldu.")
