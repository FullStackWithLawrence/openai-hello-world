SHELL := /bin/bash
CONTAINER_NAME := hello_world

ifeq ($(OS),Windows_NT)
    PYTHON = python.exe
    ACTIVATE_VENV = venv\Scripts\activate
else
    PYTHON = python3.11
    ACTIVATE_VENV = source venv/bin/activate
endif
PIP = $(PYTHON) -m pip

ifneq ("$(wildcard .env)","")
    include .env
else
    $(shell echo -e "OPENAI_API_KEY=PLEASE-ADD-ME\nENVIRONMENT=dev\n" >> .env)
endif

.PHONY: analyze pre-commit init lint clean test build release

# Default target executed when no arguments are given to make.
all: help

analyze:
	cloc . --exclude-ext=svg,json,zip --vcs=git

release:
	git commit -m "fix: force a new release" --allow-empty && git push

# -------------------------------------------------------------------------
# Install and run pre-commit hooks
# -------------------------------------------------------------------------
pre-commit:
	pre-commit install
	pre-commit autoupdate
	pre-commit run --all-files

# ---------------------------------------------------------
# create python virtual environments for dev as well
# as for the Lambda layer.
# ---------------------------------------------------------
init:
	make clean
	npm install && \
	$(PYTHON) -m venv venv && \
	$(ACTIVATE_VENV) && \
	$(PIP) install --upgrade pip && \
	$(PIP) install -r requirements/dev.txt && \
	$(PIP) install -r requirements/prod.txt && \
	deactivate && \
	pre-commit install

test:
	python -m unittest discover -s app/

lint:
	isort .
	pre-commit run --all-files
	black .
	flake8 ./app/
	pylint ./app/**/*.py

clean:
	rm -rf venv node_modules app/__pycache__ package-lock.json

build:
	docker build -t ${CONTAINER_NAME} .

run:
	source .env && \
	docker run -it -e OPENAI_API_KEY=${OPENAI_API_KEY} -e ENVIRONMENT=prod ${CONTAINER_NAME}


######################
# HELP
######################

help:
	@echo '===================================================================='
	@echo 'analyze             - generate code analysis report'
	@echo 'release             - force a new release'
	@echo 'init            - create a Python virtual environment and install dependencies'
	@echo 'test            - run Python unit tests'
	@echo 'lint            - run Python linting'
	@echo 'clean           - destroy the Python virtual environment'
