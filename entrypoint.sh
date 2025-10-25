#!/bin/bash
set -e

python manage.py migrate --noinput

if [ "$DEBUG" = "0" ]; then
    echo "Running collectstatic for production..."
    python manage.py collectstatic --noinput
fi

exec "$@"