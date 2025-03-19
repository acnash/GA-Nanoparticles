.PHONY: install test lint format clean

# Install dependencies using Poetry
install:
	poetry install

# Run pytest with Poetry
test:
	poetry run pytest -v --tb=short

# Run pytest with coverage
test-cov:
	poetry run pytest --cov=my_module --cov-report=term-missing

# Lint using flake8
lint:
	poetry run flake8 my_module

# Format code using black
format:
	poetry run black my_module tests

# Clean cached files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
