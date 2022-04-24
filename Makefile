PROJECT_NAME := $(shell basename $CURDIR)
VIRTUAL_ENVIRONMENT := $(CURDIR)/.venv
LOCAL_PYTHON := $(VIRTUAL_ENVIRONMENT)/bin/python3

define HELP
Manage $(PROJECT_NAME). Usage:

make run        - Run $(PROJECT_NAME).
make install    - Create virtual env, install dependencies, and run project.
make deploy     - Install and run script by running `make install` and `make run` in succession.
make update     - Update pip dependencies via Poetry and export output to requirements.txt.
make format     - Format code with Pythons `Black` library.
make lint       - Check code formatting with `flake8`.
make clean      - Remove cached files and lock files.

endef
export HELP


.PHONY: run install deploy update format lint clean help

requirements: .requirements.txt
env: ./.venv/bin/activate


.requirements.txt: requirements.txt
	$(shell . .venv/bin/activate && pip install -r requirements.txt)


all help:
	@echo "$$HELP"


.PHONY: run
run: env
	flask run


.PHONY: install
install:
	if [ ! -d "./.venv" ]; then python3 -m venv $(VIRTUAL_ENVIRONMENT); fi
	. .venv/bin/activate
	$(LOCAL_PYTHON) -m pip install --upgrade pip setuptools wheel
	$(LOCAL_PYTHON) -m pip install -r requirements.txt


.PHONY: deploy
deploy:
	make install
	make run


.PHONY: update
update:
	if [ ! -d "./.venv" ]; then python3 -m venv $(VIRTUAL_ENVIRONMENT); fi
	.venv/bin/python3 -m pip install --upgrade pip setuptools wheel
	poetry update
	poetry export -f requirements.txt --output requirements.txt --without-hashes


.PHONY: format
format: env
	isort --multi-line=3 .
	black .


.PHONY: lint
lint:
	flake8 . --count \
			--select=E9,F63,F7,F82 \
			--exclude .git,.github,__pycache__,.pytest_cache,.venv,logs,creds,.venv,docs,logs \
			--show-source \
			--statistics


.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name 'poetry.lock' -delete
	find . -name '*.log' -delete
	find . -name '.DS_Store' -delete
	find . -wholename 'logs/*.json' -delete
	find . -wholename '.pytest_cache' -delete
	find . -wholename '**/.pytest_cache' -delete
	find . -wholename './logs/*.json' -delete
	find . -wholename './logs' -delete
	find . -wholename '*.html' -delete
	find . -wholename '**/.webassets-cache'  -delete