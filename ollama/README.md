# Prof. Dr. Information — Ollama Kurulum ve Çalıştırma Modülü

Bu dizin, **Prof. Dr. Information** amiral gemisi medikal yapay zekâ modelini yerel bilgisayarınızda tek bir komutla Ollama motoruna kaydetmenizi ve çalıştırmanızı sağlar.

---

## 🚀 Hızlı Başlangıç

### 1. Modeli Ollama'ya Kaydetme
Aşağıdaki betiğe çift tıklayın veya terminalde çalıştırın:
```cmd
install_model.bat
```
*(Bu işlem GGUF ağırlıklarını ve 2027 Klinik Sistem İstemini sisteme entegre eder).*

### 2. Modeli Başlatma ve Sohbet Etme
```cmd
run_model.bat
```

---

## ⚙️ Yapılandırma & Çıkarım Parametreleri
* **Bağlam Uzunluğu (Context Window):** 4096 - 16384 token
* **Temperature:** 0.65 (Yüksek medikal kesinlik ve düşük rastlantısallık)
* **Top-P:** 0.90
* **Tekrarlama Cezası (Repeat Penalty):** 1.10
* **Düşünce Modu:** `<think>` CoT analitik düşünce motoru aktif.
