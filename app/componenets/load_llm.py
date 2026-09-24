from langchain_groq import ChatGroq
from app.common.logger import get_logger
from app.common.custom_exceptions import CustomException    
from app.config.config import GROQ_API_KEY

logger = get_logger(__name__)

def load_llm(model_name :str="openai/gpt-oss-120b", groq_api_key:str=GROQ_API_KEY):
    try:
        logger.info(f"Loading LLM model....")
        llm = ChatGroq(model_name=model_name, groq_api_key=groq_api_key,
        temperature = 0.8,
        max_tokens = 250
        )
        logger.info(f"Successfully loaded LLM model...")
        return llm
    except Exception as e:
        error_msg= CustomException("failed to load LLM model", e)
        logger.error(str(error_msg)) 
        return None
   
