import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
DATA_PATH ="data/" 
DB_FAISS_PATH = "vector_db/db_faiss" 

CHUNK_SIZE = 550
CHUNK_OVERLAP = 60