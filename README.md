# 📘 PolicyGPT

Vatandaş Hakları ve Resmî İşlemler Rehberi  
Yerel LLM + RAG + Basit Frontend ile çalışan bir etkileşimli kamu hizmeti asistanı.

---

## 🚀 Özellikler

- 🇹🇷 Türkçe çalışan yerel LLM (Mistral 7B - Ollama)
- 📄 PDF tabanlı resmi dökümanlardan bilgi tarama (RAG)
- ✅ Kısa, açık ve **adım adım rehber üretimi**
- 🖥️ Basit ve şık frontend (HTML + CSS)
- 🔍 Konu seçmeden direkt soru ile rehber alma desteği
- 💡 Dijital kamu farkındalığını artırma hedefi

---

## 🛠️ Kurulum

1. **Ollama'yı kur**  
   [https://ollama.com](https://ollama.com)

2. **Terminale şu komutla Mistral modelini yükle:**
   ```bash
   ollama run mistral
Projeyi klonla ve bağımlılıkları yükle:

bash
Kopyala
Düzenle
git clone https://github.com/kullaniciadi/PolicyGPT.git
cd PolicyGPT
pip install -r requirements.txt
Uygulamayı çalıştır:

bash
Kopyala
Düzenle
python app.py
Tarayıcıdan http://127.0.0.1:5000 adresine git 🎯
