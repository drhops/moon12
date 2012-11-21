#!/bin/bash
set -e

python manage.py dumpdata artful > artful.db.json
python fix_db_dump.py
mv artful.db.utf8.json artful.db.json
