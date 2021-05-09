include .env
export

###################
# Setup tasks	  #
###################
install_dev:
	pip install -e ".[dev]"

install:
	pip install .

setup_venv:
	python3.9 -m venv venv
	. venv/bin/activate

setup_dev: setup_venv install_dev

setup: setup_venv install

###################
# Testing   	  #
###################
test:
	pytest -x .

lint:
	flake8 main.py app tests
	mypy main.py app tests

cover:
	coverage run --source=app -m pytest -xv .

coverage-report: cover
	coverage report -m

bandit:
	bandit -r app main.py

bandit-ci:
	bandit -r -ll -ii app main.py

test-all: lint cover


###################
# Run       	  #
###################
run:
	./main.py