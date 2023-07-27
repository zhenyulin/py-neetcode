## CONFIG
PYTHONPATH := $(PYTHONPATH):$(pwd)
SHELL := /bin/bash -v

## COMMANDS
install:
	@poetry install

cleanup:
	@rm -rf .venv/
	@rm -rf **/__pycache__

shell:
	@poetry shell

test:
	@poetry run pytest src/ -vv -s

test-coverage:
	@poetry run pytest src/ -vv -s --cov=src --cov-report=term-missing

test-watch:
	@watchexec -e py -- poetry run pytest src/ -vv -s --picked
