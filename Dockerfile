FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat

# Устанавливаем системные зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        netcat-traditional \
        build-essential \
        libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "ad_agency.wsgi:application", "--bind", "0.0.0.0:8000"]