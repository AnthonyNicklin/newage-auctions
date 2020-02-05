release: python manage.py migrate
web: gunicorn newageauctions.wsgi:application 
worker: celery -A newageauctions.celery worker
celery_beat: celery -A newageauctions.celery beat

