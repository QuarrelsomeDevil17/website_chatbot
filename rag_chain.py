# rag_chain.py
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from vector_store import get_vector_store
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def setup_rag_chain():
    """Set up the RAG chain with DeepSeek R1 via OpenRouter"""
    # Load vector store
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    
    # Set up environment variables for OpenAI client to use OpenRouter
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
    os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"
    
    # Set up DeepSeek R1 via OpenRouter
    llm = ChatOpenAI(
        model=os.getenv("DEEPSEEK_MODEL_ID", "deepseek-chat"),
        temperature=0.1,
        max_tokens=2000,
        streaming=True
    )
    
    # Create RAG-chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )    
    return qa_chain
