@echo off
chcp 65001 > nul
echo ============================================================
echo   Prof. Dr. Information - Ollama Model Kurulum Sihirbazi
echo ============================================================
echo.

where ollama >nul 2>nul
if %errorlevel% neq 0 (
    echo [HATA] Ollama sisteminizde yuklu degil veya PATH'e eklenmemis.
    echo Lutfen https://ollama.com adresinden Ollama'yi indirip kurun.
    pause
    exit /b 1
)

echo [*] Ollama servisi kontrol ediliyor...
echo [*] Prof. Dr. Information modeli kaydediliyor...
ollama create dr-information -f Modelfile

if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo   [BASARILI] 'dr-information' basariyla kaydedildi!
    echo   Calistirmak icin: run_model.bat dosyasina tiklayin.
    echo ============================================================
) else (
    echo.
    echo [HATA] Model kaydi sirasinda bir sorun olustu.
)

pause
