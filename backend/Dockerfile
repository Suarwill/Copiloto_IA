FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para compilar paquetes y descargar
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*


COPY . .

# Descargar el modelo LLM
RUN wget -nc -O /app/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
    https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

# Instalar las dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6060

# Iniciar FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6060", "--reload"]
