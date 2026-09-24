from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from app.common.logger import get_logger
from app.common.custom_exceptions import CustomException
from app.componenets.vector_store import load_vector_store
from app.componenets.load_llm import load_llm

logger = get_logger(__name__)

CUSTOM_P = """
Answer the following medical questions in 2-3 lines maximum using only the information provided in the context.

Context:
{context}

Question:
{question}
"""

def set_prompt_c():
    return PromptTemplate(
        template=CUSTOM_P,
        input_variables=['context','question']   
    )

def create_qa_chain():
    try:
        logger.info("Loading Vector Store for your context./Q")
        db = load_vector_store()
        if db is None:
            raise CustomException("Vectorstore is not present.")

        llm = load_llm()
        if llm is None:
            raise CustomException("LLM is not Present.")


        qa_chain = RetrievalQA.from_chain_type(
            llm = llm,
            chain_type = "stuff",
            retriever = db.as_retriever(search_kwargs={"k":1}),
            chain_type_kwargs = {'prompt':set_prompt_c()}
        )
        logger.info("Successfully Created QA Chain...")
        return qa_chain
    except Exception as e:
        error_msg = CustomException("Failed to create QA chain...",e)
        logger.error(str(error_msg))
        return None