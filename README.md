poetry init
poetry add django
poetry shell
django-admin startproject config .

add gitignore - python

(poetry run) python manage.py runserver
(poetry run) python manage.py migrate
(poetry run) python manage.py createsuperuser
(poetry run) python manage.py startapp 이름
(poetry run) python manage.py makemigrations
