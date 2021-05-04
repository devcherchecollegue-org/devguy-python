include .env
export

###################
# Setup tasks	  #
###################
setup_venv:
	python3.9 -m venv venv
	. venv/bin/activate
	pip install .

setup_dev: setup_venv
	pip install -e ".[dev]"

setup:
	pip3 install .

###################
# Testing   	  #
###################
test:
	pytest -x .

lint:
	flake8 main.py app tests
	mypy main.py app tests

cover:
	coverage run --source=app -m pytest -x .

test-all: lint cover


###################
# Run       	  #
###################
run:
	./main.py