from langchain_community.chat_models import ChatLlamaCpp
# from langchain_openai import ChatOpenAI

from langchain_core.language_models.chat_models import BaseChatModel

from backend.config import LLM_MODEL_PATH

def get_llm() -> BaseChatModel:

    # --- Opción: Usar un LLM local en CPU (se usará el modelo GGUF descargado en ./models ) ---
    llm = ChatLlamaCpp(
        model_path=LLM_MODEL_PATH,
        temperature=0.1, # Un valor bajo para respuestas más fácticas y menos creativas.
        verbose=True  # Muestra información útil en la consola
    )

    # --- Opción: Usar OpenAI (requiere API key y conexión a internet) ---
    # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    return llm