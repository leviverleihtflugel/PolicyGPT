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


✅ **Test Senaryoları ve Ekran Görüntüleri**
Aşağıdaki test sorularıyla sistem başarıyla yanıt üretmektedir:

**1-İkametgah belgesi nasıl alınır?**
<img width="600" height="400" alt="555" src="https://github.com/user-attachments/assets/7c4fcef2-e3ef-4a86-937f-005e8d71da51" />

**2-SGK hizmet dökümü nereden alınır?**	
<img width="600" height="400" alt="666" src="https://github.com/user-attachments/assets/e4b61ba5-73c1-482f-b1f3-b736248c31da" />

**3-Türk vatandaşlığı nasıl alınır?**	
<img width="600" height="400" alt="777" src="https://github.com/user-attachments/assets/dfefa890-048d-47a7-9787-e712c14c4ffc" />

**4-Vergi borcu sorgulama nasıl yapılır?**
<img width="600" height="400" alt="888" src="https://github.com/user-attachments/assets/4302ce1d-e0ab-4044-84a7-9f391ccdc577" />

