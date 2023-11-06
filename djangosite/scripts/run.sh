#!/bin/sh

if [ "$VSCODE_DEV" = "1" ]; then
    echo "Backend is sleeping for infinity"
    sleep infinity

else
    set -e

    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate

    # python manage.py loaddata json_data/db.json

    uwsgi --socket :8000 --workers 2 --master --enable-threads --module config.wsgi
    # python manage.py runserver
    # python manage.py runserver 0.0.0.0:8000
fi