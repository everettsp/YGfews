.PHONY: install test clean format lint help

help:
	@echo "Available commands:"
	@echo "  make install    - Install project dependencies"
	@echo "  make test       - Run tests"
	@echo "  make format     - Format code with black"
	@echo "  make lint       - Lint code with flake8"
	@echo "  make clean      - Remove build artifacts"
	@echo "  make notebook   - Start Jupyter notebook server"

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest tests/ -v

format:
	black src/ tests/

lint:
	flake8 src/ tests/ --max-line-length=88

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/

notebook:
	jupyter notebook notebooks/
