# queries.py

from app.utils.document_loader import load_documents
from app.utils.vector_store import create_vector_store
from langchain.prompts import ChatPromptTemplate
from app.utils.vector_store import load_vector_store
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter
from dotenv import load_dotenv
import os
from app.config import (
    LLM_MODEL,
    QUERY_GENERATION_TEMPLATE,
    FINAL_ANSWER_TEMPLATE,
    RETRIVAL_TECHNIQUE,
)



# -------------------------------------------------------
#  LLM ERROR
# -------------------------------------------------------
class LLMError(Exception):
    """Raised when Groq/OpenAI/LLM API fails."""
    pass



# -------------------------------------------------------
#  LangSmith logs
# -------------------------------------------------------
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"



# -------------------------------------------------------
# Load API keys
# -------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '../../keys/.env')
load_dotenv(dotenv_path=dotenv_path)

openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")



# -------------------------------------------------------
# Load or create FAISS vector store
# -------------------------------------------------------
faiss_index_path = os.path.join(current_dir, '../../faiss_index')

if os.path.exists(faiss_index_path):
    print("Vector store found. Loading the vector store...")
    retriever = load_vector_store()
else:
    print("No vector store found. Creating a new vector store...")
    doc_splits = load_documents()
    retriever = create_vector_store(doc_splits)



# -------------------------------------------------------
# Define prompts
# -------------------------------------------------------
prompt_perspectives = ChatPromptTemplate.from_template(QUERY_GENERATION_TEMPLATE)



# -------------------------------------------------------
#  PROCESS QUESTION WITH ERROR HANDLING
# -------------------------------------------------------
def process_question(question: str):

    # Build multi-query generator
    generate_queries = (
        prompt_perspectives
        | ChatGroq(model_name=LLM_MODEL)
        | StrOutputParser()
        | (lambda x: x.split("\n\n"))
    )

    # ------------------------
    # 1) RETRIEVAL PHASE (LLM used here)
    # ------------------------
    try:
        retrieval_chain_multi_query = generate_queries | retriever.map() | RETRIVAL_TECHNIQUE
        docs = retrieval_chain_multi_query.invoke({"question": question})
    except Exception as e:
        # ANY error caused by Groq API / network / timeout
        raise LLMError(f"Error during LLM-based retrieval: {e}") from e


    # ------------------------
    # 2) FINAL ANSWER GENERATION (LLM used here)
    # ------------------------
    prompt = ChatPromptTemplate.from_template(FINAL_ANSWER_TEMPLATE)

    final_rag_chain = (
        {"context": retrieval_chain_multi_query, "question": itemgetter("question")}
        | prompt
        | ChatGroq(model_name=LLM_MODEL)
        | StrOutputParser()
    )

    try:
        ans = final_rag_chain.invoke({"question": question})
    except Exception as e:
        raise LLMError(f"Error during final LLM answer generation: {e}") from e

    return ans
