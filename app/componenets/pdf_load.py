import os
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.common.logger import get_logger
from app.common.custom_exceptions import CustomException
from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

#LOAD THE DATA FROM THE PDF FILES
def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data path  does not exist.")
        logger.info(f"Loading PDF files from {DATA_PATH}")

        loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()
        if not documents:
            logger.warning("No PDF files found ")
        else:
            logger.info(f"successfully fetched {len(documents)} no. of documents.")
        return documents
    except Exception as e:
        error_msg= CustomException("failed to load pdf files", e)
        logger.error(str(error_msg)) 
        return []



# TO CREATE CHUNKS OF DATA FROM THE PDF FILES

def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("No documents were found.")
        logger.info(f"splitting {len(documents)} documents into text")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        text_chunks = text_splitter.split_documents(documents)
        logger.info(f"generated{len(text_chunks)} of chunks.")
        return text_chunks
    except Exception as e:
        error_msg= CustomException("failed to create text chunks", e)
        logger.error(str(error_msg)) 
        return []