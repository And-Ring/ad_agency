#!/bin/bash
set -e

echo "DEBUG=$DEBUG"
echo "Waiting for PostgreSQL at $DJANGO_DB_HOST:$DJANGO_DB_PORT..."

until nc -z "$DJANGO_DB_HOST" "$DJANGO_DB_PORT"; do
  echo "PostgreSQL not ready yet..."
  sleep 1
done

echo "PostgreSQL is up — running migrations..."
python manage.py migrate --noinput

if [ "${DEBUG:-1}" = "0" ]; then
    echo "Running collectstatic for production..."
    python manage.py collectstatic --noinput
fi

echo "Starting application..."
exec "$@"