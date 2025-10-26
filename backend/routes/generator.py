from fastapi import APIRouter, Body
from services.generator_chain import generator_chain

router = APIRouter()

@router.post("/")
async def generate(data: dict = Body(...)):
    type_ = data.get("type", "essay")
    topic = data.get("topic", "")
    result = generator_chain.run(type=type_, topic=topic)
    return {"output": result}
