from app.componenets import vector_store
from app.componenets.pdf_load import load_pdf_files, create_text_chunks
from app.componenets.vector_store import load_vector_store, save_vector_store
from app.common.logger import get_logger
from app.common.custom_exceptions import CustomException
from app.config.config import DB_FAISS_PATH
import os


logger = get_logger(__name__)

def inject_data():
    try:
        logger.info("checking for existing vector store...")
        
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Existing vector store found...")
            return load_vector_store()
        logger.info("no vector store found... so creating a new one...")
        
        documents = load_pdf_files()
        text_chunks = create_text_chunks(documents)
        vector_store = save_vector_store(text_chunks)
        return vector_store
    except Exception as e:
        error_msg = CustomException("Failed to create  database.", e)
        logger.error(str(error_msg))
        return None

if __name__ == "__main__":
    inject_data()