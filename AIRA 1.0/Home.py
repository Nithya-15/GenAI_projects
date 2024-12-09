import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import app


def load_styles(file_path):
    with open(file_path, "r") as f:
        return f.read()
styles=load_styles("styles.md")
st.markdown(styles, unsafe_allow_html=True)

# Landing page design
st.markdown("<div class='title'>AIRA 1.0 🤖</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Accelerating Knowledge Retrieval from Scientific Literature</div>", unsafe_allow_html=True)

# Displaying descriptive boxes for capabilities
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>How can AIRA help You?</h2>", unsafe_allow_html=True)

# Creating columns to organize the capabilities
capabilities = [
    {
        "title": "Smart Document Search",
        "description": "Find relevant sections from your PDFs instantly using semantic search.",
        "emoji": "🔍",
    },
    {
        "title": "Document Similarity Search",
        "description": "Identify reference documents and retrieve their names, links, and key details.",
        "emoji": "🔗",
    },
    {
        "title": "Contextual Chat",
        "description": "Engage in a Q&A session based on the loaded research papers.",
        "emoji": "💬",
    },
    {
        "title": "Keyword Extraction",
        "description": "Identify key topics and phrases from your documents.",
        "emoji": "📌",
    },
]

# Displaying capabilities in two columns
cols = st.columns(2)
for i, capability in enumerate(capabilities):
    with cols[i % 2]:  
        st.markdown(f"""
        <div class="box">
            <h3>{capability['emoji']} {capability['title']}</h3>
            <p>{capability['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Call-to-action button
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""<div class="button">
            <a href="/Chat" target="_self">
            Get Started
            </a>
            </div>""", unsafe_allow_html=True)

