release: python manage.py migrate
web: gunicorn newageauctions.wsgi:application 
worker: celery -A newageauctions.celery worker --loglevel=info
celery_beat: celery -A newageauctions.celery beat --loglevel=info 

