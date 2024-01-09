
SHELL := /bin/bash
REPO_NAME := openai-hello-world

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
    $(shell echo -e "OPENAI_API_KEY=SET-ME-PLEASE\nENVIRONMENT=dev\nDOCKERHUB_USERNAME=localhost\nDOCKERHUB_ACCESS_TOKEN=SET-ME-PLEASE\n" >> .env)
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
# create python virtual environments for prod
# ---------------------------------------------------------
init:
	make clean
	npm install && \
	$(PYTHON) -m venv venv && \
	$(ACTIVATE_VENV) && \
	$(PIP) install --upgrade pip && \
	$(PIP) install -r requirements/prod.txt && \
	deactivate && \
	pre-commit install

# ---------------------------------------------------------
# create python virtual environments for dev
# ---------------------------------------------------------
init-dev:
	make init
	$(ACTIVATE_VENV) && \
	$(PIP) install -r requirements/dev.txt && \
	deactivate

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

docker-build:
	source .env && \
	docker build -t ${DOCKERHUB_USERNAME}/${REPO_NAME} .

docker-push:
	source .env && \
	docker tag ${DOCKERHUB_USERNAME}/${REPO_NAME} ${DOCKERHUB_USERNAME}/${REPO_NAME}:latest && \
	echo "${DOCKERHUB_ACCESS_TOKEN}" | docker login --username=${DOCKERHUB_USERNAME} --password-stdin && \
	docker push ${DOCKERHUB_USERNAME}/${REPO_NAME}:latest

docker-run:
	source .env && \
	docker run -it -e OPENAI_API_KEY=${OPENAI_API_KEY} -e ENVIRONMENT=prod ${DOCKERHUB_USERNAME}/${REPO_NAME}:latest


######################
# HELP
######################

help:
	@echo '===================================================================='
	@echo 'analyze         - generate code analysis report'
	@echo 'release         - force a new GitHub release'
	@echo 'init            - create a Python virtual environment and install prod dependencies'
	@echo 'init-dev        - install dev dependencies'
	@echo 'test            - run Python unit tests'
	@echo 'lint            - run Python linting'
	@echo 'clean           - destroy the Python virtual environment'
	@echo 'docker-build    - build the Docker image'
	@echo 'docker-push     - push the Docker image to DockerHub'
	@echo 'docker-run      - run the Docker image'
