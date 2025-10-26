from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chatbot import router as chatbot_router
from routes.rag_reader import router as rag_router
from routes.generator import router as generator_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot_router, prefix="/api/chatbot")
app.include_router(rag_router, prefix="/api/rag")
app.include_router(generator_router, prefix="/api/generator")

@app.get("/")
def root():
    return {"message": "EduGenAI Backend Running"}
