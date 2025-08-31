# backup/Dockerfile

# Используем образ postgres, так как в нем уже есть pg_dump
FROM postgres:15

# Устанавливаем cron и gzip
RUN apt-get update && apt-get install -y cron gzip

# Копируем наш скрипт бэкапа и делаем его исполняемым
COPY backup.sh /usr/local/bin/backup.sh
RUN chmod +x /usr/local/bin/backup.sh

# Копируем файл с расписанием cron
COPY crontab /etc/cron.d/backup-cron

# Даем правильные права файлу расписания
RUN chmod 0644 /etc/cron.d/backup-cron

# Создаем crontab и запускаем cron в режиме foreground
RUN crontab /etc/cron.d/backup-cron
CMD ["cron", "-f"]