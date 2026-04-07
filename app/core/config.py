import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    VECTOR_DB_PATH = "vectorstore/faiss_index"

settings = Settings()
