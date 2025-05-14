# app/routers/chat_router.py
from fastapi import APIRouter, Request, Body
from app.services.chat_service import chat

router = APIRouter()

@router.post("/")
async def chat_endpoint(history: list[dict] = Body(...)):
    history, error = chat(history)
    if error:
        return {"error": error}
    return {"history": history}
