from langchain_huggingface import HuggingFaceEmbeddings

from app.common.logger import get_logger
from app.common.custom_exceptions import CustomException

logger = get_logger(__name__)

def get_embedding_model():
    try:
        logger.info("Initializing HuggingFace Embeddings model...")
        model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        logger.info("HuggingFace Embeddings model initialized successfully.")
        return model
        
    except Exception as e:
        error_msg = CustomException("Failed to create embeddings.", e)
        logger.error(str(error_msg))
        return None

