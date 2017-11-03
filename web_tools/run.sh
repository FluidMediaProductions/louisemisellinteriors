#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --no-input -c

gunicorn --bind 0.0.0.0:8000 --workers 5 web_tools.wsgi