from app.utils.document_loader import load_documents
from app.services.embeddings import create_vectorstore

docs = load_documents()
create_vectorstore(docs)

print("FAISS index created successfully!")
