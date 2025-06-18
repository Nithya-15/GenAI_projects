from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import chat, documents, search

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="AIRA 1.0 API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router)
app.include_router(documents.router)
app.include_router(search.router)
