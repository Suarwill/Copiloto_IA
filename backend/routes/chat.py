from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import logging

from backend.services.rag_service import query_rag

router = APIRouter()

class ChatRequest(BaseModel):
    pregunta: str

@router.post("/")
async def handle_chat(request: ChatRequest):

    if not request.pregunta or not request.pregunta.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La pregunta no puede estar vacía."
        )
    
    try:
        respuesta = query_rag(request.pregunta)
        return {"respuesta": respuesta}
    except Exception as e:
        logging.error(f"Error en el endpoint de chat: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocurrió un error al procesar la pregunta."
        )