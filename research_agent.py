import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")

RESEARCH_TOPIC = """
Ana karakter verildiğinde 5–7 dakikalık çocuk çizgi film bölümü üretebilen bulut tabanlı otonom çizgi film stüdyosu için en sade kurulabilir sistem mimarisini araştır.
Araçları API, n8n bağlantısı, custom code ihtiyacı, maliyet, karakter tutarlılığı, ses, dudak senkronu, video üretimi, montaj, yayın ve performans analizi açısından karşılaştır.
Sonuçta tek bir V1 mimari öner.
"""

PROMPT = f"""
CLOUD CARTOON STUDIO RESEARCH AGENT V1

Sen profesyonel bir AI çizgi film stüdyosu sistem araştırma agentısın.

Görev:
{RESEARCH_TOPIC}

Kurallar:
- Gerçek web araştırması yap.
- Fiyat uydurma.
- Kaynak bulamazsan "fiyat doğrulanamadı" yaz.
- Kesin bilgi, tahmin ve yorumu ayır.
- Amaç araç listesi değil, kurulabilir sistem mimarisi çıkarmak.
- Maksimum 30 kaynak mantığıyla çalış.
- Sonuç karar verdirmeli.
- V1 video üretmesin; önce mimari seçsin.

Şu araçları değerlendir:
fal.ai, Replicate, RunPod, ComfyUI, Kling, Runway, Pika, Luma,
Cartoon Animator, Reallusion, Blender, Toon Boom, Adobe Character Animator,
OpenAI TTS, ElevenLabs, Azure TTS, Edge TTS,
Wav2Lip, MuseTalk, LivePortrait, Sync Labs, HeyGen,
n8n, Google Sheets, Telegram, YouTube API.

Rapor formatı:

ANALİZ:
PROBLEM:
NET DÜŞÜNCE:
ÖNERİLEN V1 SİSTEM MİMARİSİ:
N8N İLE YAPILACAK İŞLER:
CUSTOM CODE İLE YAPILACAK İŞLER:
OPENAI API İLE YAPILACAK İŞLER:
BROWSER AGENT İLE YAPILACAK İŞLER:
GÖRSEL / VİDEO ÜRETİM ARAÇLARI:
2D ÇİZGİ FİLM / RIG ARAÇLARI:
SES VE DUDAK SENKRONU:
DATABASE / HAFIZA YAPISI:
ÜRETİM AKIŞI:
PERFORMANS GERİ BESLEME SİSTEMİ:
MALİYET KONTROLÜ:
RİSKLER:
İLK MVP:
BUGÜNÜN NET KARARI:
BUGÜN YAPILACAK TEK AKSİYON:
PUAN:
NETLİK:
"""

def run_research():
    print("Gerçek web araştırmalı Research Agent çalışıyor...")

    response = client.responses.create(
        model=MODEL_NAME,
        tools=[{"type": "web_search"}],
        input=PROMPT
    )

    report = response.output_text

    date_code = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"cloud_cartoon_web_research_report_{date_code}.txt"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(report)

    print("\nRapor oluşturuldu:")
    print(file_name)
    print("\n--- RAPOR ---\n")
    print(report)

if __name__ == "__main__":
    run_research()