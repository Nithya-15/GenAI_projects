from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.retrieval import search_documents
from app.services.embeddings import extract_keywords


router = APIRouter(prefix="/search", tags=["Search"])

class SearchRequest(BaseModel):
    query: str

@router.post("/smart-search")
async def smart_search(request: SearchRequest):
    """
    Perform a smart search over the documents using vector similarity.
    """
    try:
        results = search_documents(request.query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/keywords")
async def keyword_extraction(request: SearchRequest):
    """
    Extract keywords from the given query/document text.
    """
    try:
        keywords = extract_keywords(request.query)
        return {"keywords": keywords}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
