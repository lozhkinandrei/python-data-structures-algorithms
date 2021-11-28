format:
	black .

lint:
	flake8 .

test:
	coverage run -m unittest

coverage:
	coverage report && coverage html
