import pickle
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

VECTORS_FILE = "faiss_store.pkl"

def load_vectors(file_path=VECTORS_FILE):
    """
    Load the FAISS vector store from the pickle file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Vector store file '{file_path}' not found.")
    with open(file_path, "rb") as f:
        vectors = pickle.load(f)
    print("FAISS vector store loaded successfully!")
    return vectors

def search_documents(query, k=5):
    """
    Perform a similarity search over the vector store given a user query.
    """
    vectors = load_vectors()
    results = vectors.similarity_search(query, k=k)

    documents = []
    for doc in results:
        documents.append({
            "content": doc.page_content,
            "metadata": doc.metadata
        })

    return documents
