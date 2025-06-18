from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import pickle

def create_vectors(pdf_folder, output_path):
    """
    Load PDFs from the specified folder, split them into chunks, generate embeddings,
    store them in a FAISS vector store, and pickle the store to disk.
    """
    print(f"Scanning PDFs in folder: {pdf_folder}")
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    print(f"PDF files found: {len(pdf_files)}")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    loader = PyPDFDirectoryLoader(pdf_folder)
    docs = loader.load()
    print(f"Number of documents loaded: {len(docs)}")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)
    print(f"Number of chunks created: {len(final_documents)}")

    vectors = FAISS.from_documents(final_documents, embeddings)
    print("FAISS vector store created successfully!")

    with open(output_path, "wb") as f:
        pickle.dump(vectors, f)
    print(f"FAISS vector store saved to: {output_path}")


def extract_keywords(text):
    dummy_keywords = text.split()[:5] 
    return dummy_keywords
