.PHONY: install install-dev clean clean-all test lint format docs dist all help

# Default target when just running 'make'
.DEFAULT_GOAL := help

# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
VENV := .venv
ACTIVATE := source $(VENV)/bin/activate
PYTEST := pytest
RUFF := ruff
MYPY := mypy
PYTHON_FILES := llamaduck/ tests/ setup.py

help:
	@echo "LlamaDuck Pro - Makefile targets:"
	@echo ""
	@echo "  install      - Install package without development dependencies"
	@echo "  install-dev  - Install package with development dependencies"
	@echo "  clean        - Remove build artifacts, caches, and test coverage files"
	@echo "  clean-all    - Remove build artifacts, caches, virtual environment, etc."
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting tools"
	@echo "  format       - Format code with ruff"
	@echo "  docs         - Generate documentation"
	@echo "  dist         - Build package distributions"
	@echo "  all          - Run all checks (lint, format, test)"
	@echo ""

install:
	$(PIP) install -e .

install-dev:
	$(PIP) install -e ".[dev,test]"

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +

clean-all: clean
	rm -rf $(VENV)/
	rm -rf docs/_build/

test:
	$(PYTEST) -xvs tests/ --cov=llamaduck --cov-report=term-missing

lint:
	$(RUFF) check $(PYTHON_FILES)
	$(MYPY) llamaduck/

format:
	$(RUFF) format $(PYTHON_FILES)

docs:
	@echo "Documentation generation will be implemented in future versions"

dist:
	$(PYTHON) -m build

all: format lint test

# Install hook
install-hooks:
	@echo "Setting up pre-commit hooks..."
	@if [ ! -f .git/hooks/pre-commit ]; then \
		echo '#!/bin/sh\nmake format lint' > .git/hooks/pre-commit; \
		chmod +x .git/hooks/pre-commit; \
		echo "Pre-commit hook installed."; \
	else \
		echo "Pre-commit hook already exists."; \
	fi 