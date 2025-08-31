FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .

RUN apt-get update && apt-get install -y dos2unix postgresql-client && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Создаем скрипт инициализации
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh && \
    dos2unix /app/entrypoint.sh

EXPOSE 8000
CMD ["/app/entrypoint.sh"]