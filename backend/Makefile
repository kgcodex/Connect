# Use bash 
SHELL := /bin/bash

# Variables
PYTHON := python 
MANAGE := $(PYTHON) manage.py

# Targets
.PHONY: run migrate test venv

# Create virtual environment and install dependencies
venv:
	$(PYTHON) -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

# Run Django ASGI server
run-asgi:
	uvicorn connect_backend.asgi:application --reload --port 8000

# Run Django development server
run:
	$(MANAGE) runserver 

	
# Migration 
migrate: 
	$(MANAGE) makemigrations
	$(MANAGE) migrate

test:
	pytest

cov:
	pytest --cov=api \
	       --cov-report=html \
	       --cov-report=term \
	       --cov-report=annotate

seed:
	$(MANAGE) seed_db