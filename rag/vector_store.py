# rag/vector_store.py
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os

PERSIST_DIR = os.path.join("rag", "chroma_db")

def get_vector_store(persist_directory: str = PERSIST_DIR):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    return vectordb
