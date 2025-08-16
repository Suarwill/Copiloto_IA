from fastapi.middleware.cors import CORSMiddleware

def add_middleware_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8501", "http://frontend:8501"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )