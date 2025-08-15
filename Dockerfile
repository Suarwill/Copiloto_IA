# Usar una imagen base de Python oficial.
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Instalar dependencias del sistema que puedan ser necesarias para compilar
# paquetes como llama-cpp-python.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requerimientos primero para aprovechar el cache de Docker.
COPY requirements.txt .

# Instalar PyTorch para CPU para evitar las pesadas dependencias de CUDA.
# Esto es crucial para mantener la imagen ligera y compatible con CPU.
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Instalar el resto de las dependencias.
# La variable CMAKE_ARGS es necesaria para que llama-cpp-python se compile correctamente.
ENV CMAKE_ARGS="-DLLAMA_CUBLAS=OFF"
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación.
COPY ./backend /app/backend

# Exponer el puerto en el que se ejecutará la aplicación.
EXPOSE 8000
