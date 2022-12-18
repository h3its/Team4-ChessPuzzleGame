#!/bin/sh

export FLASK_APP=chess

# run db migrations
echo "Running database migrations..."
flask db upgrade

echo "Starting app..."
gunicorn --config gunicorn_config.py chess:app
