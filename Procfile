release: python manage.py migrate
web: gunicorn newageauctions.wsgi:application 
main_worker: python manage.py celery worker --beat --loglevel=info

