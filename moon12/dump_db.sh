#!/bin/bash
set -e

DJANGO_SETTINGS_MODULE=moon12.settings python manage.py dumpdata --format=json-pretty artful > artful.db.json
#python manage.py dumpdata artful > artful.db.json
#python fix_db_dump.py
#mv artful.db.utf8.json artful.db.json
