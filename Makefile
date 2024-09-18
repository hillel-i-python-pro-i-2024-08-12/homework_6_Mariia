.PHONY: run purge lint

# Specify the shell for running commands
SHELL := /bin/bash

# Run the homework application inside Docker
d-homework-i-run:
	@echo "Running homework in Docker"
	docker compose up --build

# Purge Docker containers, images, volumes, and orphans
d-homework-i-purge:
	@echo "Purging Docker containers, images, volumes, and orphans"
	docker compose down --rmi all --volumes --remove-orphans

# Lint the codebase using isort, black, and flake8
lint:
	@echo "Running isort..."
	poetry run isort .
	@echo "Running black..."
	poetry run black .
	@echo "Running flake8..."
	poetry run flake8 .
