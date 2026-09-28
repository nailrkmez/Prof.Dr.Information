# Prof. Dr. Information — 2027 Multimodal Clinical AI & Medical Decision Support System
## 2027.2 Ultra Enterprise Edition | Zero-Hallucination & Perpetual Memory Architecture

[![Language](https://img.shields.io/badge/Language-English%20%7C%20Turkish-blue.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT%20%2F%20Healthcare-green.svg)](LICENSE)
[![Zero-Hallucination](https://img.shields.io/badge/Standard-Zero--Hallucination%20Clinical-red.svg)](#)
[![Multimodal](https://img.shields.io/badge/Perception-Multimodal%20Vision%20%26%20OCR-purple.svg)](#)

---

## 🌍 Language / Dil Seçimi
- [English Documentation](#-english-documentation)
- [Türkçe Dokümantasyon](#-t%C3%BCrk%C3%A7e-dok%C3%BCmantasyon)

---

# 🇬🇧 English Documentation

### Overview
**Prof. Dr. Information** is an autonomous, multimodal medical AI operating at 2027 international clinical standards (AHA/ACC, ESC, KDIGO, GOLD, NCCN, Surviving Sepsis 2026/2027). Designed with zero-hallucination protocols, perceptual vision capabilities, and persistent conversational memory, it functions as a Senior Clinical Fellow and Autonomous Medical Documentation Specialist.

### 🌟 Key Capabilities
1. **Active Cognitive Reasoning (`<think>...</think>`):**
   * Executes systematic root-cause pathophysiological reasoning before rendering clinical recommendations.
   * Rejects shallow, monotonous bullet lists; explains differential diagnoses in eloquent, professional clinical prose.
2. **Multimodal Perception & Document OCR:**
   * Reads, analyzes, and contextualizes medical imagery (X-Rays, ECGs, CT/MRI scans, and laboratory panels).
3. **Continuous Learning & Persistent Memory:**
   * Retains full conversational context across sessions.
   * Dynamic **Knowledge Vault**: Instantly ingest new clinical papers, guidelines, or case reports without retraining.
4. **Emergency Red Flag Safeguards:**
   * Enforces strict contraindication protocols (e.g., prohibition of nitrates/morphine in right ventricular infarction; avoidance of debridement in stable heel eschars).

---

### 📂 Directory Architecture
```
├── github/                 # Open-source community collaboration & documentation
│   ├── README.md           # Bilingual global project documentation
│   ├── CONTRIBUTING.md     # Clinical verification & contribution guidelines
│   └── data_pipeline_50gb.py # 50 GB streaming LLM data pipeline
│
├── ollama/                 # Local offline deployment engine
│   ├── Modelfile           # Enterprise reasoning & multimodal system prompt
│   ├── install_model.bat   # One-click model registration wizard
│   ├── run_model.bat       # Instant terminal session launcher
│   └── README.md           # Deployment manual
│
├── webui/                  # Standalone Multimodal Web Interface
│   ├── index.html          # Sleek glassmorphism dark mode UI with vision support
│   ├── style.css           # Premium responsive stylesheet
│   ├── app.js              # Real-time memory & file-upload interaction engine
│   ├── server.py           # Local REST API with continuous learning knowledge vault
│   └── start_webui.bat     # One-click web interface launcher (http://localhost:8080)
│
└── models/                 # Unified clinical model binary
    └── Prof_Dr_Information_2027.Q4_K_M.gguf
```

---

### 🚀 Getting Started

#### Option 1: Web Interface (Recommended)
Double-click `webui/start_webui.bat` or run:
```bash
cd webui
python server.py
```
Open in browser: `http://localhost:8080`

#### Option 2: Ollama Local CLI
Double-click `ollama/install_model.bat` then `ollama/run_model.bat`.

---

### 🤝 Contributing
Clinicians, biomedical engineers, and AI researchers are encouraged to submit new decision trees, differential diagnostic pathways, and clinical test cases. Please review [CONTRIBUTING.md](CONTRIBUTING.md).

---
---

# 🇹🇷 Türkçe Dokümantasyon

### Genel Bakış
**Prof. Dr. Information**; 2027 uluslararası tıp standartlarında (AHA/ACC, ESC, KDIGO, GOLD, Surviving Sepsis 2026/2027) çalışan, sıfır halüsinasyon, görsel/belge okuma algısı ve kalıcı sohbet hafızasına sahip otonom Kıdemli Yardımcı Hekim ve Multimodal Tıbbi Karar Destek Sistemidir.

### 🌟 Temel Yetenekler
1. **Derin Bilişsel Muhakeme (`<think>...</think>`):**
   * Her klinik vaka ve soruda patofizyolojik sebep-sonuç ilişkilerini adım adım analiz eder.
   * Kuru ve robotik listeler yerine, kıdemli hekim konsültasyon üslubunda akıcı paragraflar yazar.
2. **Çok Boyutlu Görsel & Tahlil Algısı (Multimodal Vision/OCR):**
   * Yüklenen laboratuvar tahlillerini, EKG şeritlerini ve radyolojik fotoğrafları okur ve klinik tabloyla birleştirir.
3. **Kalıcı Sohbet Hafızası & Sürekli Öğrenme:**
   * Önceki hasta konuşmalarını ve geçmişi asla unutmaz.
   * Sol panelden yeni makale, protokol veya rapor yükleyerek modelin bilgi hazinesini anında genişletebilirsiniz.
4. **Kırmızı Bayrak & Katı Kontrendikasyon Güvenliği:**
   * İnme (FAST), STEMI, anafilaksi gibi tablolarda derhal 112 acil protokolünü devreye alır.
   * Kritik klinik kontrendikasyonları (Sağ ventrikül enfarktüsünde nitrat yasağı, stabil topuk eskarında debridman yasağı vb.) tavizsiz uygular.

---

### 🚀 Hızlı Başlangıç

#### Seçenek 1: Modern Web Arayüzü (Önerilen)
`webui/start_webui.bat` dosyasına çift tıklayın veya:
```bash
cd webui
python server.py
```
Tarayıcınızda açın: `http://localhost:8080`

#### Seçenek 2: Ollama Komut Satırı
`ollama/install_model.bat` ile modeli kurun, ardından `ollama/run_model.bat` ile sohbeti başlatın.

---

### 🤝 Katkıda Bulunma
Yeni klinik algoritmalar, acil protokolleri veya doğrulama testleri eklemek isteyen hekimler ve araştırmacılar [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyebilirler.

---

### 📄 Lisans / License
Bu proje, sağlık ekosistemine küresel fayda sağlamak amacıyla MIT Lisansı ile yayınlanmıştır.
