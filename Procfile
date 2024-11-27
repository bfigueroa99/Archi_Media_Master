release: mkdir -p media_masters/static && python manage.py collectstatic --noinput
web: gunicorn archi-media-master.wsgi --log-file -
