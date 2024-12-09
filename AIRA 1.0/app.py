import streamlit as st
import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
import pickle
from xlsx_to_dict import pdf_links_dict

# Load environment variables 
from dotenv import load_dotenv
load_dotenv()

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize session state 
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Define LLM and Prompt
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)
prompt = ChatPromptTemplate.from_template("""
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question:
    <context>
    {context}
    <context>
    Question: {input}
""")


def load_vectors_with_huggingface(file_path="faiss_store_hf2.pkl"):
    with open(file_path, "rb") as f:
        faiss_store = pickle.load(f)
    return faiss_store


def initialize_session_with_huggingface():
    if "vectors" not in st.session_state:
        st.session_state.vectors = load_vectors_with_huggingface()
        print("Hugging Face vectors loaded successfully!")

initialize_session_with_huggingface()

links_dict=pdf_links_dict()


def load_styles(file_path):
    with open(file_path, "r") as f:
        return f.read()
    
styles=load_styles("styles.md")
st.markdown(styles, unsafe_allow_html=True)

st.markdown("<div class='title'>AIRA 1.0 🤖</div>", unsafe_allow_html=True)
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(f"<div class='chat-message user'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-message assistant'>{message['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

def handle_user_input(user_input):
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(f"<div class='chat-message user'>{user_input}</div>", unsafe_allow_html=True)

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    with st.chat_message("assistant"):

        response = retrieval_chain.invoke({"input": user_input})
        st.markdown(f"<div class='chat-message assistant'>{response['answer']}</div>", unsafe_allow_html=True)
        

    st.session_state.messages.append({"role": "assistant", "content": response['answer']})

    
    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response['context']):
            # Retrieve metadata and link
            doc_name = doc.metadata.get('filename', 'Unknown Filename') 
            link = links_dict.get(doc_name, 'Not available')

            with st.container():
                col1, col2 = st.columns([1, 3]) 
                with col1:
                    st.markdown("#### Document Details")
                    st.write(f"**Name**: {doc_name}")
                    if link != 'Not available':
                        st.write(f"**[Web Link]({link})**")
                    else:
                        st.write("**Web Link**: Not available")

                with col2:
                    st.markdown("#### Document Content")
                    st.write(doc.page_content)

                st.markdown("---")




user_input = st.chat_input("Ask a question about the research paper")


if user_input:
    handle_user_input(user_input)


