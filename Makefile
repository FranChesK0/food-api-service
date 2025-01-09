.PHONY: help format lint check pc run

.DEFAULT_GOAL := help

help:
	@echo "Usage: make [TARGET]"
	@echo "Targets:"
	@echo "  help    Display this help message"
	@echo "  format  Format code with Black and Isort"
	@echo "  lint    Lint code with Flake8 and MyPy"
	@echo "  check   Run format and lint targets"
	@echo "  pc      Run pre-commit hooks"
	@echo "  run     Run application"

format:
	isort .
	black .

lint:
	flake8 .
	mypy .

check: format lint

pc:
	pre-commit run --all-files

run:
	python food/src/main.py
