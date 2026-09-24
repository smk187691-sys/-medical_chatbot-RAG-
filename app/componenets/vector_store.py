from langchain_community.vectorstores import FAISS
import os
from app.componenets.embeddings import get_embedding_model
from app.common.logger import get_logger
from app.common.custom_exceptions import CustomException
from app.config.config import DB_FAISS_PATH 

logger = get_logger(__name__)

def load_vector_store():
    try:
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FAISS_PATH):
            logger.info("Loading existing vector database...")
            return FAISS.load_local(DB_FAISS_PATH, embedding_model,allow_dangerous_deserialization=True)
        else:
            logger.warning("NO vector database found...")

    except Exception as e:
        error_msg = CustomException("Failed to LOAD vector store.", e)
        logger.error(str(error_msg))
        return error_msg


def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No text chunks were found....")
        logger.info("generating your new vector store...")
        embedding_model = get_embedding_model()

        db = FAISS.from_documents(text_chunks, embedding_model)
        logger.info("saving vector store to disk...")
        db.save_local(DB_FAISS_PATH)
        logger.info("vector store saved successfully.")
        return db
    except Exception as e:
        error_msg = CustomException("Failed to create vector store.", e)
        logger.error(str(error_msg))
        # return error_msg