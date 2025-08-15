from fastapi.middleware.cors import CORSMiddleware

def add_middleware_cors(app):
    app.addMiddleware(
        CORSMiddleware,
        allow_origins=["*"],  # Especificar las IP de origen permitidas.
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )