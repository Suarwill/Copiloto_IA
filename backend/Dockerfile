FROM python:3.11-slim

# Backend
WORKDIR /app

# Instalar dependencias del sistema necesarias para compilar paquetes y descargar
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instalar las dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Crear carpeta de modelos y descargar
RUN mkdir -p /app/models && \
    wget -nc -O /app/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
    https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

EXPOSE 6060

# Iniciar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6060", "--reload"]
