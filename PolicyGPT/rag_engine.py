from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

import os

# LLM ve embedder
llm = Ollama(model="mistral")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Soru-cevap fonksiyonu
def query(question):
    all_docs = []
    pdf_files = [
        "data/ikametgah.pdf",
        "data/sgk.pdf",
        "data/vatandaslik.pdf",
        "data/vergi.pdf"
    ]

    for path in pdf_files:
        if os.path.exists(path):
            loader = PyPDFLoader(path)
            all_docs.extend(loader.load())

    if not all_docs:
        return {
            "steps": "Hiçbir PDF dosyası yüklenemedi.",
            "scenario": "",
            "summary": ""
        }

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(all_docs)

    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    prompt = (
        f"Soru: {question}\n"
        f"Lütfen sadece Türkçe olarak sade ve adım adım bir rehber üret. "
        f"Senaryo yazma. Yalnızca uygulanabilir adımlar üret. "
        f"Kısa, net ve madde madde şekilde sırala:\n"
        f"1. ..., 2. ..., 3. ... gibi, alt alta olacak şekilde."
    )

    response = qa_chain.run(prompt).strip()

    return {
        "steps": response,
        "scenario": "",
        "summary": ""
    }
