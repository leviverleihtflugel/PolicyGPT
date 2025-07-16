# 📘 PolicyGPT: Vatandaş Hakları ve Resmi İşlemler Rehberi

PolicyGPT, vatandaşların e-Devlet işlemleri gibi resmi konularda adım adım rehberlik alabileceği bir yapay zeka uygulamasıdır. LLM ve RAG teknolojilerini kullanarak vatandaşlık, ikametgah, SGK ve vergi işlemleriyle ilgili sadeleştirilmiş rehberler üretir.

## 🚀 Özellikler

- ✅ Etkileşimli adım adım rehber
- ✅ PDF içeriklerinden RAG (Retrieval-Augmented Generation)
- ✅ Türkçe doğal dil desteği
- ✅ Yerel çalışabilir (internet gerekmez)
- ✅ Basit ve kullanıcı dostu arayüz

---

## 🧠 Kullanılan Teknolojiler

| Bileşen | Açıklama |
|--------|---------|
| **LLM** | [Ollama](https://ollama.com) + Mistral modeli (yerel çalışır) |
| **RAG** | LangChain + FAISS + HuggingFace Embeddings |
| **Frontend** | Flask + HTML/CSS |
| **Veri** | Yerel PDF mevzuat dokümanları (`data/` klasörü) |

---

## 🛠️ Kurulum

1. **Ollama'yı kur**  
   [https://ollama.com](https://ollama.com)
<img width="500" height="300" alt="111" src="https://github.com/user-attachments/assets/2b800830-b165-426e-ba37-6ba3f2473fb7" />

3. **Terminale şu komutla Mistral modelini yükle:**
   ```bash
   ollama run mistral
<img width="500" height="300" alt="2222" src="https://github.com/user-attachments/assets/791c02d8-f7c4-4cc4-ab11-8408bc951f16" />

4. **Projeyi indir ve terminalden klasörü aç:**
   ```bash
   cd PolicyGPT

3. **Sanal ortam oluştur:**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows için
   # source venv/bin/activate  # MacOS/Linux için
<img width="500" height="300" alt="333" src="https://github.com/user-attachments/assets/5fc4294e-b3ed-4734-85d6-e2139a8fb437" />

4. **Projeye gerekli bağımlılıkları yükle::**
   ```bash
   pip install -r requirements.txt
   
4. **Uygulamayı çalıştır ve tarayıcıdan adrese git:**   
   ```bash
   python app.py
   Tarayıcıdan http://127.0.0.1:5000 adresine git 🎯
<img width="500" height="300" alt="4444" src="https://github.com/user-attachments/assets/1e5eb2e1-4e48-4353-a841-3d1b3fa81380" />

---

📂 **Klasör Yapısı**
   ```bash
    PolicyGPT/
   ├── app.py                     # Flask ana uygulama dosyası
   ├── rag_engine.py              # RAG (Retrieval-Augmented Generation) fonksiyonları
   ├── requirements.txt           # Gerekli Python paketleri
   │
   ├── data/                      # PDF mevzuat belgeleri
   │   ├── ikametgah.pdf
   │   ├── sgk.pdf
   │   ├── vatandaslik.pdf
   │   └── vergi.pdf
   │
   ├── static/                    # CSS gibi statik dosyalar
   │   └── style.css
   │
   ├── templates/                 # HTML arayüz dosyası
   │   └── index.html
   │
   ├── venv/                      # 📌 Python sanal ortam klasörü (Git'e eklenmez)
   │
   └── README.md                  # Proje açıklaması ve kurulum rehberi
```
---


✅ **Test Senaryoları**
Aşağıdaki test sorularıyla sistem başarıyla yanıt üretmektedir:

Soru	Beklenen Çıktı
İkametgah belgesi nasıl alınır?	E-Devlet’e giriş, belge oluşturma adımları
SGK hizmet dökümü nereden alınır?	E-Devlet SGK hizmetleri adımları
Türk vatandaşlığı nasıl alınır?	Vatandaşlık başvuru belgeleri ve süreç
Vergi borcu sorgulama nasıl yapılır?	Gelir İdaresi ve E-Devlet entegrasyonu

Her bir soru, PDF rehber içeriğine uygun olarak sadeleştirilmiş madde madde sonuçlar üretir.
