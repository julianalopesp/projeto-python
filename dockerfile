# Use uma imagem base do Python
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o diretório de trabalho
COPY . .

# Expôr a porta em que o aplicativo irá rodar (por exemplo, 8000 se for um servidor web)
EXPOSE 8000

# Comando para iniciar o aplicativo
CMD ["python", "app.py"]
