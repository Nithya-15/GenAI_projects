# Research Paper Q&A with Groq and Llama3

This Streamlit application allows users to query research papers using **Retrieval-Augmented Generation (RAG)** with the **Llama3 model** powered by Groq. The application supports question-answering based on the content of research papers loaded from PDF files, embedding the documents into a vector database using **OpenAI Embeddings** and **FAISS**. 

![alt text](<Screenshot 2024-10-11 at 3.34.43 PM.png>)

## Features
- Load and preprocess research papers from PDFs.
- Embed documents using **OpenAI Embeddings** and store them in a **FAISS** vector store.
- Retrieve relevant chunks from the research papers based on user queries.
- Generate accurate responses using the **Llama3** model with **Groq**.
- Display the relevant document chunks retrieved during the similarity search.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Streamlit
- `dotenv` for environment variable management

### Clone the repository
```bash
git clone <repository-url>
cd <repository-directory>



