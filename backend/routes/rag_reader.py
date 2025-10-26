from fastapi import APIRouter, UploadFile, Form
from services.rag_chain import store_document, query_document

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    store_document(file_path)
    return {"status": "uploaded"}

@router.post("/query")
async def query(question: str = Form(...)):
    answer = query_document(question)
    return {"answer": answer}
