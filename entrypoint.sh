#!/bin/bash
set -e

until nc -z "$DJANGO_DB_HOST" "$DJANGO_DB_PORT"; do
  echo "Waiting for PostgreSQL at $DJANGO_DB_HOST:$DJANGO_DB_PORT..."
  sleep 1
done

python manage.py migrate --noinput

if [ "$DEBUG" = "0" ]; then
    echo "Running collectstatic for production..."
    python manage.py collectstatic --noinput
fi

exec "$@"