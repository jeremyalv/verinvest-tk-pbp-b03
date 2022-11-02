web: gunicorn verinvest.wsgi --log-file -
release: sh -c 'python manage.py makemigrations && python manage.py migrate'