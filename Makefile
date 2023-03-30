## CONFIG
PYTHONPATH := $(PYTHONPATH):$(pwd)
SHELL := /bin/bash -v

## VARIABLES
VIRTUAL_ENV_NAME := $(shell poetry env info -p | rev | cut -d'/' -f1 | rev)

## COMMANDS
install:
	@poetry install

cleanup:
	@rm .coverage
	@rm -rf **/__pycache__
	@poetry env remove python

shell:
	@poetry shell

test:
	@poetry run pytest src/ -vv -s

test-watch:
	@watchman-make -p 'src/**/*.py' -r 'poetry run pytest src/ -vv -s --picked'

test-coverage:
	@poetry run pytest src/ -vv -s --cov=src --cov-report=term-missing

test-coverage-watch:
	@poetry run pytest src/ -vv -s --cov=src --cov-report=term-missing --picked
