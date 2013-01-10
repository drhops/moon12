#!/bin/bash
set -e

DJANGO_SETTINGS_MODULE=moon12.settings python manage.py loaddata artful artful.db.json
