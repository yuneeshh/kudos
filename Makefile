.PHONY: run migrate makemigrations superuser shell format lint test

PYTHON=python
MANAGE=python manage.py

run:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

shell:
	$(MANAGE) shell

install:
	pip install -r requirements.txt

test:
	$(MANAGE) test

format:
	black .

lint:
	flake8 .

clean:
	find . -name "*.pyc" -exec rm -f {} \;
