import os
import urllib.request

from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.language_models.chat_models import BaseChatModel

from config import LLM_MODEL_PATH

MODEL_URL = "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

def ensure_model_exists():
    if not os.path.exists(LLM_MODEL_PATH):
        print(f"[INFO] Modelo no encontrado. Descargando desde:\n{MODEL_URL}")
        os.makedirs(os.path.dirname(LLM_MODEL_PATH), exist_ok=True)
        try:
            urllib.request.urlretrieve(MODEL_URL, LLM_MODEL_PATH)
            print("[INFO] Modelo descargado exitosamente.")
        except Exception as e:
            print(f"[ERROR] No se pudo descargar el modelo: {e}")
            raise RuntimeError("Fallo la descarga del modelo")
    else:
        print("[INFO] Modelo ya disponible localmente.")

def get_llm() -> BaseChatModel:
    # Verifica si el modelo existe antes de crear el LLM
    ensure_model_exists()

    # Inicializa el modelo con el archivo local
    llm = ChatLlamaCpp(
        model_path=LLM_MODEL_PATH,
        temperature=0.1,
        verbose=True
    )

    return llm
