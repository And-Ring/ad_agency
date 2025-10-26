#!/bin/bash

# Ждём, пока база станет доступна
until nc -z $DJANGO_DB_HOST $DJANGO_DB_PORT; do
  sleep 1
done

# Применяем миграции и собираем статические файлы
python manage.py migrate
python manage.py collectstatic --noinput

# Запуск сервера
gunicorn ad_agency.wsgi:application --bind 0.0.0.0:8000