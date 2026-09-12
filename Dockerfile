# Imagem base oficial e leve do Python (guia: https://docs.docker.com/language/python/)
FROM python:3.12-slim

WORKDIR /app

# Copia só o requirements primeiro para aproveitar o cache de camadas do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Agora copia o código da aplicação
COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
