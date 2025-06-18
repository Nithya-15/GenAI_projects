from fastapi import APIRouter, Body
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    user_query: str

llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template("""
Answer the question based on context:
<context>
{context}
</context>
Question: {input}
""")

def get_answer(user_input):
    return {"answer": f"Simulated response to: {user_input}", "context": []}

@router.post("/ask")
async def ask_question(request: ChatRequest):
    response = get_answer(request.user_query)
    return response
