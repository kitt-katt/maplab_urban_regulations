#!/bin/bash
set -e

echo "Waiting for PostgreSQL to be ready..."
while ! pg_isready -h maplab_urban_db -U urban_user -d urban_db; do
  echo "PostgreSQL is not ready yet. Waiting..."
  sleep 2
done
echo "PostgreSQL is ready!"

echo "Running Django migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || echo "Superuser already exists or creation failed"

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
