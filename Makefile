
serve:
	python manage.py serve && . .env

test:
	python -m doctest test_doctest.py -v

