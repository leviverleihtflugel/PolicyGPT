from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

import os

def get_pdf_path(topic):
    topic_file_map = {
        "ikametgah": "data/ikametgah.pdf",
        "sgk": "data/sgk.pdf",
        "vatandaslik": "data/vatandaslik.pdf",
        "vergi": "data/vergi.pdf"
    }
    return topic_file_map.get(topic.lower())

llm = Ollama(model="mistral")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def query(question, topic):
    pdf_path = get_pdf_path(topic)
    if not pdf_path or not os.path.exists(pdf_path):
        return {
            "steps": "Belirtilen konuya ait PDF dosyası bulunamadı.",
            "scenario": "",
            "summary": ""
        }

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    prompt = (
    f"Soru: {question}\n"
    f"Lütfen sadece Türkçe olarak sade ve adım adım bir rehber üret. "
    f"Yalnızca Türkçe yaz. Kısa, açık ve uygulanabilir maddelerden oluşsun."
)

    response = qa_chain.run(prompt).strip()

    return {
        "steps": response,
        "scenario": "",
        "summary": ""
    }
