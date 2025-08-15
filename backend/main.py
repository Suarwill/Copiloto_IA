from fastapi import FastAPI
from backend.middlewares import add_middleware_cors
from backend.routes import router_upload, router_chat

app = FastAPI(
    title="Copiloto Conversacional",
    description="Una API para cargar PDFs y hacer preguntas en lenguaje natural sobre su contenido.",
    version="1.0.0"
)

# Middleware
add_middleware_cors(app)

# Rutas
app.include_router(router_upload, prefix="/upload", tags=["Carga de PDFs"])
app.include_router(router_chat, prefix="/chat", tags=["Consultas"])

# Ruta base
@app.get("/")
def read_raiz():
    return {"mensaje": "Bienvenido al Backend: API en FastAPI"}