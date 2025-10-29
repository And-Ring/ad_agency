#!/bin/bash

# Установить dev-зависимости
pip install --no-cache-dir -r requirements.dev.txt

# Запустить Django
exec python manage.py runserver 0.0.0.0:8000