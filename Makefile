create_user:
	python3 manage.py createsuperuser --username=admin --email=admin@mail.ru

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

