from fastapi import FastAPI
from backend.middlewares.cors import addMiddlewareCors

from backend.routes.upload import router as routerUpload
from backend.routes.chat import router as routerChat

app = FastAPI(
    title="Copiloto Conversacional",
    description="Una API para cargar PDFs y hacer preguntas en lenguaje natural sobre su contenido.",
    version="1.0.0"
)

# Middleware
addMiddlewareCors(app)

# Rutas
app.include_router(routerUpload, prefix="/upload", tags=["Carga de PDFs"])
app.include_router(routerChat, prefix="/chat", tags=["Consultas"])

# Ruta base
@app.get("/")
def readRoot():
    return {"mensaje": "Bienvenido al Backend: API en FastAPI"}