from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil
from app.services.embeddings import create_vectors

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_FOLDER = "uploaded_pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file and store it in the uploads folder.
    """
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"message": f"File '{file.filename}' uploaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create-embeddings")
async def create_embeddings():
    """
    Process all PDFs in the uploads folder and create embeddings.
    """
    try:
        create_vectors(UPLOAD_FOLDER, "faiss_store.pkl")
        return {"message": "Embeddings created successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
