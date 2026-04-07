from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from app.core.config import settings

def get_embeddings():
    return OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

def create_vectorstore(documents):
    embeddings = get_embeddings()
    db = FAISS.from_documents(documents, embeddings)
    db.save_local(settings.VECTOR_DB_PATH)
    return db

def load_vectorstore():
    embeddings = get_embeddings()
    return FAISS.load_local(settings.VECTOR_DB_PATH, embeddings)
