#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uçtan Uca LLM Veri Hattı (Data Pipeline)
Hugging Face Streaming API ile 50 GB dengeli korpusu indirir,
filtreler, BPE ile tokenize eder ve eğitim için binary (.bin) memmap dosyalarına yazar.
"""

import os
import sys
import json
import time
import argparse
import numpy as np
import tiktoken
from datasets import load_dataset
from tqdm import tqdm

# 50 Gigabayt hedef sınır (Byte cinsinden: 50 * 1024^3)
TARGET_RAW_BYTES = 50 * 1024 * 1024 * 1024

# Amiral gemisi açık kaynak modellerin (Llama, Qwen) veri harmanı oranları
SOURCES = [
    {
        "id": "fineweb_edu",
        "dataset_name": "HuggingFaceFW/fineweb-edu",
        "split": "train",
        "text_field": "text",
        "ratio": 0.50,  # %50 Kaliteli eğitici genel web korpusu (~25 GB)
        "description": "FineWeb-Edu web korpusu"
    },
    {
        "id": "the_stack_code",
        "dataset_name": "bigcode/the-stack-smol-xs",
        "split": "train",
        "text_field": "content",
        "ratio": 0.25,  # %25 Çok dilli kod ve teknik dökümantasyon (~12.5 GB)
        "description": "The Stack kod havuzu"
    },
    {
        "id": "open_web_math",
        "dataset_name": "open-web-math/open-web-math",
        "split": "train",
        "text_field": "text",
        "ratio": 0.15,  # %15 Matematiksel akıl yürütme metinleri (~7.5 GB)
        "description": "OpenWebMath analitik verisi"
    },
    {
        "id": "ultrachat_sft",
        "dataset_name": "HuggingFaceH4/ultrachat_200k",
        "split": "train_sft",
        "text_field": "messages",
        "ratio": 0.10,  # %10 Talimat, soru-cevap ve diyalog (~5 GB)
        "description": "UltraChat çok turlu diyalog verisi"
    }
]

def clean_and_validate(text: str) -> str:
    """Temel sezgisel kalite filtreleme uygular."""
    if not text or not isinstance(text, str):
        return ""
    text = text.strip()
    # 150 karakterden kısa anlamsız parçaları ve aşırı kısa satırları ele
    if len(text) < 150:
        return ""
    words = text.split()
    if len(words) < 25:
        return ""
    # Ortalama kelime uzunluğu kontrolü (bozuk kod/metin veya spam eleme)
    avg_word_len = sum(len(w) for w in words) / len(words)
    if avg_word_len < 3.0 or avg_word_len > 12.0:
        return ""
    return text

def parse_entry_text(entry: dict, field_name: str) -> str:
    """Farklı şema formatlarını tekilleştirilmiş metne çevirir."""
    raw_val = entry.get(field_name)
    if isinstance(raw_val, str):
        return clean_and_validate(raw_val)
    elif isinstance(raw_val, list):
        # UltraChat benzeri role-content formatı
        convo_lines = []
        for msg in raw_val:
            role = msg.get("role", "user")
            content = msg.get("content", "").strip()
            if content:
                convo_lines.append(f"<|im_start|>{role}\n{content}<|im_end|>")
        combined = "\n".join(convo_lines)
        return clean_and_validate(combined)
    return ""

def main():
    parser = argparse.ArgumentParser(description="50 GB LLM Data Pipeline & Tokenizer")
    parser.add_argument("--output_dir", type=str, default="./processed_dataset", help="Çıktı klasörü")
    parser.add_argument("--val_ratio", type=float, default=0.01, help="Validation veri ayrım oranı")
    parser.add_argument("--tokenizer", type=str, default="gpt2", help="Tiktoken şablonu (gpt2, cl100k_base)")
    parser.add_argument("--batch_tokens", type=int, default=2_000_000, help="Diske yazma tampon boyutu")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    train_bin_path = os.path.join(args.output_dir, "train.bin")
    val_bin_path = os.path.join(args.output_dir, "val.bin")
    meta_json_path = os.path.join(args.output_dir, "meta.json")

    print(f"[1/4] Tokenizer başlatılıyor: {args.tokenizer}")
    enc = tiktoken.get_encoding(args.tokenizer)
    eot_token = enc.eot_token

    train_tokens_buffer = []
    val_tokens_buffer = []
    total_train_tokens = 0
    total_val_tokens = 0
    total_raw_bytes = 0

    train_file = open(train_bin_path, "wb")
    val_file = open(val_bin_path, "wb")

    start_time = time.time()
    pbar = tqdm(total=TARGET_RAW_BYTES, unit="B", unit_scale=True, desc="Ham Veri İndirme & İşleme")

    try:
        for src in SOURCES:
            if total_raw_bytes >= TARGET_RAW_BYTES:
                break

            target_src_bytes = int(TARGET_RAW_BYTES * src["ratio"])
            current_src_bytes = 0
            print(f"\n--> Kaynak bağlanıyor: {src['id']} ({src['description']})")
            print(f"    Hedef hacim: {target_src_bytes / (1024**3):.2f} GB")

            try:
                ds = load_dataset(src["dataset_name"], split=src["split"], streaming=True)
            except Exception as e:
                print(f"    [!] {src['id']} veri setine bağlanılamadı: {e}. Sonraki kaynağa geçiliyor.")
                continue

            for entry in ds:
                text = parse_entry_text(entry, src["text_field"])
                if not text:
                    continue

                encoded_str = text.encode("utf-8")
                doc_bytes = len(encoded_str)

                # Tokenizasyon
                tokens = enc.encode_ordinary(text)
                tokens.append(eot_token)

                # Train/Validation ayrımı (Rastgele hash veya orana dayalı deterministik ayrım)
                if np.random.rand() > args.val_ratio:
                    train_tokens_buffer.extend(tokens)
                else:
                    val_tokens_buffer.extend(tokens)

                total_raw_bytes += doc_bytes
                current_src_bytes += doc_bytes
                pbar.update(doc_bytes)

                # Tampon dolduğunda diske binary (uint16) olarak boşalt
                if len(train_tokens_buffer) >= args.batch_tokens:
                    arr = np.array(train_tokens_buffer, dtype=np.uint16)
                    arr.tofile(train_file)
                    total_train_tokens += len(train_tokens_buffer)
                    train_tokens_buffer.clear()

                if len(val_tokens_buffer) >= (args.batch_tokens // 10):
                    arr = np.array(val_tokens_buffer, dtype=np.uint16)
                    arr.tofile(val_file)
                    total_val_tokens += len(val_tokens_buffer)
                    val_tokens_buffer.clear()

                if current_src_bytes >= target_src_bytes or total_raw_bytes >= TARGET_RAW_BYTES:
                    break

        # Kalan tamponları diske boşalt
        if train_tokens_buffer:
            np.array(train_tokens_buffer, dtype=np.uint16).tofile(train_file)
            total_train_tokens += len(train_tokens_buffer)
            train_tokens_buffer.clear()

        if val_tokens_buffer:
            np.array(val_tokens_buffer, dtype=np.uint16).tofile(val_file)
            total_val_tokens += len(val_tokens_buffer)
            val_tokens_buffer.clear()

    finally:
        train_file.close()
        val_file.close()
        pbar.close()

    elapsed = time.time() - start_time
    total_tokens = total_train_tokens + total_val_tokens

    meta = {
        "tokenizer": args.tokenizer,
        "vocab_size": enc.n_vocab,
        "dtype": "uint16",
        "total_train_tokens": total_train_tokens,
        "total_val_tokens": total_val_tokens,
        "total_tokens": total_tokens,
        "processed_raw_bytes": total_raw_bytes,
        "processed_raw_gb": round(total_raw_bytes / (1024**3), 2),
        "elapsed_seconds": round(elapsed, 2)
    }

    with open(meta_json_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=4)

    print("\n" + "=" * 60)
    print("VERİ HATTI BAŞARIYLA TAMAMLANDI")
    print("=" * 60)
    print(f"Toplam İşlenen Ham Boyut : {meta['processed_raw_gb']} GB")
    print(f"Toplam Üretilen Token     : {total_tokens:,}")
    print(f"Train Tokens             : {total_train_tokens:,}")
    print(f"Val Tokens               : {total_val_tokens:,}")
    print(f"Eğitim Dosyaları         : {train_bin_path}")
    print(f"                           {val_bin_path}")
    print(f"Metadata Dosyası         : {meta_json_path}")
    print(f"Tamamlanma Süresi        : {elapsed / 60:.2f} dakika")
    print("=" * 60)

if __name__ == "__main__":
    main()
