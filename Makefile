install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --nbval --cov=script --cov=mylib test_*.py

format:
	black *.py

lint:
	ruff check *.py

all: install lint format test
