from pathlib import Path

# --- Paths / Rutas ---
BASE_DIR = Path(__file__).resolve().parent.parent
VECTOR_STORE_PATH = str(BASE_DIR / "data")
MODELS_PATH = str(BASE_DIR / "models")

# --- Embeddings ---
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2" # Buen rendimiento en local
EMBEDDING_DEVICE = "cpu"  # Cambiar a "cuda" si se tiene una GPU configurada

# --- LLM ---
LLM_MODEL_FILENAME = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
LLM_MODEL_PATH = str(Path(MODELS_PATH) / LLM_MODEL_FILENAME)

# --- RAG ---
RETRIEVER_K = 3  # Número de chunks relevantes a recuperar
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150