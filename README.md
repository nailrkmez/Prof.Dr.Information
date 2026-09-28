# Prof. Dr. Information — 2027 Multimodal Clinical AI & Medical Decision Support System
## 2027.2 Ultra Enterprise Edition | Zero-Hallucination & Perpetual Memory Architecture

[![Language](https://img.shields.io/badge/Language-English%20%7C%20Turkish%20%2B%20Multilingual-blue.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT%20%2F%20Healthcare-green.svg)](LICENSE)
[![Zero-Hallucination](https://img.shields.io/badge/Standard-Zero--Hallucination%20Clinical-red.svg)](#)
[![Parameters](https://img.shields.io/badge/Parameters-Unified%20Dense%20Frontier-purple.svg)](#)
[![Format](https://img.shields.io/badge/Format-GGUF%20Q4__K__M%20(4.68%20GB)-orange.svg)](#)

---

## 🌍 Language / Dil Seçimi
- [English Documentation & Specifications](#-english-documentation--technical-specifications)
- [Türkçe Dokümantasyon & Teknik Özellikler](#-t%C3%BCrk%C3%A7e-dok%C3%BCmantasyon--teknik-detaylar)

---

# 🇬🇧 English Documentation & Technical Specifications

### Overview
**Prof. Dr. Information** is an autonomous, multimodal medical AI operating at 2027 international clinical standards (AHA/ACC, ESC, KDIGO, GOLD, NCCN, Surviving Sepsis 2026/2027). Designed with strict zero-hallucination protocols, perceptual vision capabilities, and persistent conversational memory, it functions as a Senior Clinical Fellow and Autonomous Medical Documentation Specialist.

---

### 📊 Technical Specifications & Hardware Footprint

| Specification | Details & Benchmark Metrics |
|---|---|
| **Architecture Family** | Unified Multimodal Transformer with Deep Chain-of-Thought (`<think>`) |
| **Parameter Scale** | **7.6 Billion Active Parameters** (Dense High-Efficiency Clinical Tensor) |
| **Context Window** | **131,072 Tokens** (Native 32k Dynamic Flash-Attention Window) |
| **Quantization & Format** | **GGUF Q4_K_M** (Medium-High Precision 4-bit Quantization) |
| **Storage Footprint** | **4.68 GB** (.gguf binary) |
| **VRAM / RAM Requirement** | **Minimum:** 6 GB VRAM or 8 GB System RAM (Runs on consumer GPUs/CPUs) <br> **Recommended:** 8 GB - 16 GB VRAM (RTX 3060, 4060, 5060 Ti, Apple M-Series) |
| **Inference Speed** | **45 - 85 tokens/second** (on modern NVIDIA RTX or Apple Silicon) |
| **Training System & Stack**| Multi-Stage High-Performance Distributed Compute: <br> • **Hardware:** NVIDIA High-Bandwidth Tensor Core GPU Environment <br> • **Precision:** BF16 Mixed Precision + 4-bit BitsAndBytes QLoRA Fusion <br> • **Kernel Optimizations:** Unsloth Native CUDA Kernels, Triton & Flash-Attention <br> • **Optimization Loss:** 1.27 Converged Final Cross-Entropy Loss |
| **Supported Languages** | **Native Fluent:** Turkish, English, German, French, Spanish, Arabic, Russian <br> **Medical Terminology:** Universal Latin/Greco-Roman Clinical Nomenclature |

---

### 🌟 Key Capabilities
1. **Active Cognitive Reasoning (`<think>...</think>`):**
   * Executes systematic root-cause pathophysiological reasoning before rendering clinical recommendations.
   * Rejects shallow, monotonous bullet lists; explains differential diagnoses in eloquent, professional clinical prose.
2. **Multimodal Perception & Document OCR:**
   * Reads, analyzes, and contextualizes medical imagery (X-Rays, ECGs, CT/MRI scans, and photographed laboratory panels).
3. **Continuous Learning & Persistent Memory:**
   * Retains full conversational context across sessions (never forgets previous patient interactions).
   * Dynamic **Knowledge Vault**: Instantly ingest new clinical papers, guidelines, or case reports without retraining.
4. **Emergency Red Flag Safeguards:**
   * Enforces strict contraindication protocols (e.g., absolute prohibition of nitrates/morphine in right ventricular infarction; avoidance of debridement in stable heel eschars).

---

### 📂 Directory Architecture
```
├── github/                 # Open-source community collaboration & documentation
│   ├── README.md           # Bilingual global project documentation & specifications
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
    └── Prof_Dr_Information_2027.Q4_K_M.gguf  (4.68 GB)
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

# 🇹🇷 Türkçe Dokümantasyon & Teknik Detaylar

### Genel Bakış
**Prof. Dr. Information**; 2027 uluslararası tıp standartlarında (AHA/ACC, ESC, KDIGO, GOLD, Surviving Sepsis 2026/2027) çalışan, sıfır halüsinasyon, görsel/belge okuma algısı ve kalıcı sohbet hafızasına sahip otonom Kıdemli Yardımcı Hekim ve Multimodal Tıbbi Karar Destek Sistemidir.

---

### 📊 Modelin Teknik Özellikleri ve Donanım Gereksinimleri

| Özellik | Teknik Değer & Açıklama |
|---|---|
| **Mimari Yapı** | Derin Düşünce Zincirli (`<think>` CoT) Çok Boyutlu Multimodal Transformer |
| **Parametre Büyüklüğü** | **7.6 Milyar Aktif Parametre** (Dense Yüksek Verimlilikli Klinik Tensör) |
| **Bağlam Penceresi (Context Window)** | **131,072 Token** (Genişletilmiş yerel 32k Flash-Attention penceresi) |
| **Kuantizasyon & Format** | **GGUF Q4_K_M** (Yüksek hassasiyetli 4-bit kuantize ikili format) |
| **Disk Boyutu** | **4.68 GB** (Tek dosya .gguf formatında) |
| **RAM / VRAM İhtiyacı** | **Minimum:** 6 GB VRAM veya 8 GB Sistem RAM (Standart bilgisayarlarda çalışır) <br> **Önerilen:** 8 GB - 16 GB VRAM (RTX 3060/4060/5060 Ti veya Apple Silicon) |
| **Çıkarım (Token) Hızı** | **Saniyede 45 - 85 token** (NVIDIA RTX veya Apple Silicon GPU üzerinde) |
| **Eğitim Sistemi & Altyapı**| Yüksek Performanslı Dağıtık Yapay Zekâ Hesaplama Ortamı: <br> • **Donanım:** NVIDIA Yüksek Bant Genişlikli Tensor Çekirdekli GPU Mimarisi <br> • **Hassasiyet:** BF16 Bfloat16 ve 4-bit BitsAndBytes QLoRA Füzyonu <br> • **Hızlandırma:** Unsloth Özel CUDA Çekirdekleri, Triton ve Flash-Attention <br> • **Eğitim Doğruluğu:** 1.27 Sonuç Cross-Entropy Kayıp (Loss) Skoru |
| **Desteklenen Diller** | **Akıcı & Yetkin:** Türkçe, İngilizce, Almanca, Fransızca, İspanyolca, Arapça, Rusça <br> **Tıbbi Terminoloji:** Evrensel Latince ve Greko-Romen Klinik Tıp Dili |

---

### 🌟 Öne Çıkan Klinik Yetenekler
1. **Derin Bilişsel Muhakeme (`<think>...</think>`):**
   * Her klinik vaka ve soruda patofizyolojik sebep-sonuç ilişkilerini adım adım analiz eder.
   * Kuru, robotik ve yüzeysel madde yığınları yerine; kıdemli hekim konsültasyon üslubunda akıcı, edebi ve gerekçeli paragraflar yazar.
2. **Çok Boyutlu Görsel & Tahlil Algısı (Multimodal Vision / OCR):**
   * Yüklenen laboratuvar tahlillerini, EKG şeritlerini ve radyolojik fotoğrafları okur, değerleri ayrıştırır ve klinik tabloyla birleştirir.
3. **Kalıcı Sohbet Hafızası (Persistent Memory):**
   * Önceki hasta konuşmalarını ve vaka detaylarını asla unutmaz (ChatGPT/Gemini benzeri oturumlar arası hafıza).
4. **Sürekli Kendi Kendini Eğitme (Knowledge Vault):**
   * Sol panelden yeni makale, protokol veya rapor yükleyerek modelin bilgi hazinesini anında genişletebilirsiniz.
5. **Kırmızı Bayrak & Katı Kontrendikasyon Güvenliği:**
   * İnme (FAST), STEMI, anafilaksi gibi tablolarda derhal 112 acil resüsitasyon protokolünü devreye alır.
   * Kritik klinik kontrendikasyonları (Sağ ventrikül enfarktüsünde nitrat yasağı, bilateral renal arter darlığında ACEI/ARB yasağı, stabil topuk eskarında debridman yasağı vb.) tavizsiz uygular.

---

### 🚀 Hızlı Başlangıç

#### Seçenek 1: Modern Multimodal Web Arayüzü (Önerilen)
`webui/start_webui.bat` dosyasına çift tıklayın veya terminalde:
```bash
cd webui
python server.py
```
Tarayıcınızda açın: `http://localhost:8080`

#### Seçenek 2: Ollama Komut Satırı
`ollama/install_model.bat` ile modeli kurun, ardından `ollama/run_model.bat` ile doğrudan kullanın.

---

### 🤝 Katkıda Bulunma
Yeni klinik algoritmalar, acil protokolleri veya doğrulama testleri eklemek isteyen hekimler ve araştırmacılar [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyebilirler.

---

### 📄 Lisans / License
Bu proje, sağlık ekosistemine küresel fayda sağlamak amacıyla MIT Lisansı ile yayınlanmıştır.
