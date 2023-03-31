clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}

isort:
	- isort --skip-glob=.tox --reverse-sort --profile=black .

flake8:
	- flake8 --exclude='.tox','__init__.py','venv/','tests/' --extend-exclude='*_pb2*.py' .

blue:
	- blue . --exclude=['.tox','__init__.py','venv/','tests/']

lint: isort blue flake8

release:
	- rm -r dist build
	- python3 setup.py sdist bdist_wheel
	- python3 -m twine upload --repository gitlab dist/*
