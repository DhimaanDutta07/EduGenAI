from fastapi import APIRouter, Body
from services.chatbot_chain import chatbot_chain

router = APIRouter()

@router.post("/")
async def chat(data: dict = Body(...)):
    message = data.get("message", "")
    result = chatbot_chain.predict(input=message)
    return {"response": result}
