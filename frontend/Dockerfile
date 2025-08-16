FROM python:3.11-slim

#Frontend
WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get clean
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Puerto 8501 (puerto por defecto de Streamlit)
EXPOSE 8501

# Iniciar Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]