# rag/ingest_pdf.py
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

PDF_DIR = os.path.join("rag", "brand_docs")
DB_DIR = os.path.join("rag", "chroma_db")

def ingest_pdfs(pdf_dir: str = PDF_DIR, persist_dir: str = DB_DIR, chunk_size: int = 800, chunk_overlap: int = 150):
    all_docs = []
    if not os.path.exists(pdf_dir):
        raise FileNotFoundError(f"{pdf_dir} not found. Create and put your PDFs there.")

    for file in os.listdir(pdf_dir):
        if file.lower().endswith(".pdf"):
            path = os.path.join(pdf_dir, file)
            loader = PyPDFLoader(path)
            docs = loader.load()
            all_docs.extend(docs)

    if not all_docs:
        print("No PDFs found to ingest.")
        return

    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(all_docs)

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=persist_dir)
    vectordb.persist()
    print(f"✅ Ingested {len(chunks)} chunks into vector DB at {persist_dir}")

if __name__ == "__main__":
    ingest_pdfs()
