from fastapi.middleware.cors import CORSMiddleware

def addMiddlewareCors(app):
    app.addMiddleware(
        CORSMiddleware,
        allow_origins=["*"],  # Especificar las IP de origen permitidas.
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )