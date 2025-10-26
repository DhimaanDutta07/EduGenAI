import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ""))

from backend.routes.chatbot import router as chatbot_router
from backend.routes.rag_reader import router as rag_router
from backend.routes.generator import router as generator_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot_router, prefix="/api/chatbot")
app.include_router(rag_router, prefix="/api/rag")
app.include_router(generator_router, prefix="/api/generator")

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def index_page():
    return FileResponse("frontend/index.html")

@app.get("/chatbot")
def chatbot_page():
    return FileResponse("frontend/chatbot.html")

@app.get("/generator")
def generator_page():
    return FileResponse("frontend/generator.html")

@app.get("/rag")
def rag_page():
    return FileResponse("frontend/rag.html")
