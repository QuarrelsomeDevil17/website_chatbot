from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List
import os

def load_documents(folder_path: str) -> List[Document]:
    """Load all documents from a folder."""
    documents = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if file.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
                loaded = loader.load()
                if loaded:
                    documents.extend(loaded)
            elif file.endswith('.txt'):
                loader = TextLoader(file_path)
                loaded = loader.load()
                if loaded:
                    documents.extend(loaded)
            else:
                print(f"Unsupported file type: {file}")
                continue
        except Exception as e:
            print(f"Failed to load {file_path}: {e}")

    return documents

def split_documents(documents: List[Document], chunk_size=1000, chunk_overlap=200) -> List[Document]:
    """Split documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(documents)
