from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List
import os

def create_vector_store(documents: List[Document], store_path: str = "faiss_store"):
    """Create and save a FAISS vector store from documents"""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(store_path)
    return vector_store

def load_vector_store(store_path: str = "faiss_store"):
    """Load an existing FAISS vector store"""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    return FAISS.load_local(store_path, embeddings, allow_dangerous_deserialization=True)

def get_vector_store(store_path: str = "faiss_store", documents_folder: str = "documents"):
    """Get vector store - creates new if doesn't exist, otherwise loads existing."""
    if os.path.exists(store_path):
        return load_vector_store(store_path)
    else:
        from document_processor import load_documents, split_documents
        documents = load_documents(documents_folder)
        split_docs = split_documents(documents)
        print(f"Documents loaded: {len(documents)}")
        print(f"Chunks created: {len(split_docs)}")
        return create_vector_store(split_docs, store_path)

