
python3 manage.py migrate
python3 manage.py collectstatic
gunicorn app.wsgi:application \
  --bind 0.0.0.0:80
