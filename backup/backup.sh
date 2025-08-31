#!/bin/bash

# Устанавливаем переменные окружения для pg_dump
export PGPASSWORD=$POSTGRES_PASSWORD

# Создаем бэкап с сжатием gzip и временной меткой в имени файла
echo "Creating backup for database $POSTGRES_DB..."
pg_dump -h maplab_urban_db -U $POSTGRES_USER -d $POSTGRES_DB | gzip > /backups/backup_$(date +%Y-%m-%d_%H-%M-%S).sql.gz

echo "Backup created successfully."