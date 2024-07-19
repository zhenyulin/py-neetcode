# ------------------------------------- NOTES ------------------------------------- #

## LINKS
#
# * justfile docs: https://just.systems/man/en/chapter_1.html
# * cheapsheet: https://cheatography.com/linux-china/cheat-sheets/justfile/

## DIFFERENT SYNTAXES - INSIDE/OUTSIDE RECIPE
#
# justfile syntax applies outside recipe (command level), shell syntax applies within recipe
#
# example - reference variable
# outside recipe - referenced by VAR_NAME: `PROJECT_NAME := file_stem(PYTHONPATH)`
# inside recipe - referenced by $VAR_NAME: `ipykernel install --name $PROJECT_NAME`

## FUNCTIONS
# justfile functions are preferred over shell functions for cross-platform compatibility
# justfile function docs: https://just.systems/man/en/chapter_31.html

## TIPS
# - '-command' to ignore errors: https://just.systems/man/en/chapter_30.html
# - use * for packing arguments, e.g. *FLAGS,*PARAMETERS *, $FLAGS to access

# ----------------------------------------------------------------------------------- #

#
## SETUP
#

# CONFIG
set ignore-comments
set shell := ["bash", "-uc"] # -u to throw errors for unset variables, -c so that string commands can be run
set windows-shell := ["bash", "-uc"]

#
## COMMANDS - Development
#

# list available commands
[group('dev')]
@default:
    just --list --unsorted

### Install

[macos]
@_install_python:
    pyenv install -s # -s to skip if set python version is already installed

[windows]
@_install_python:
    VERSION_MATCH="^ *$(pyenv local)" # start with any number of spaces and minor version from .python-version
    PYTHON_VERSION=$(pyenv install --list | grep $VERSION_MATCH | tail -n 1 | xargs) # get the latest patch version
    pyenv install $PYTHON_VERSION -q

@_set_poetry_python:
    poetry env use $(pyenv which python) # ensure poetry to use pyenv python (avoid anaconda conflicts)
    poetry env info | grep -A 5 "Base" | grep -E "Python|Path"

# resolve lockfile conflicts
[group('dev')]
lockfile:
    poetry lock --no-update

# install python, dependencies, pre-commit hooks
[group('dev')]
@install:
    just _install_python
    just _set_poetry_python
    just lockfile
    poetry install
    poetry run pre-commit install --install-hooks

### Cleanup

@_cleanup_tooling_cache:
    rm -rf .mypy_cache
    rm -rf .ruff_cache

@_cleanup_test_report:
    rm -rf .benchmarks/
    rm -rf .coverage

@_cleanup_pycache:
    rm -rf src/__pycache__
    rm -rf src/**/__pycache__
    rm -rf tests/__pycache__
    rm -rf tests/**/__pycache__

# remove .venv, python & tooling cache, test reports
[group('dev')]
[confirm("cleanup .venv and build & tooling cache? (y/n)")]
cleanup:
    just _cleanup_tooling_cache
    just _cleanup_test_report
    just _cleanup_pycache
    rm -rf .venv/

### Check

# run code quality checks
[group('dev')]
@check:
    poetry run ruff check src tests --fix
    poetry run mypy src

# run code quality checks with file watcher
[group('dev')]
@check-watch:
    watchexec -n -r -w src -w tests -w mypy.ini -w ruff.toml --clear -- just check

#
## COMMANDS - Test
#

# run test (exclude benchmark and online tests)
[group('test')]
@test:
    poetry run pytest tests/ -vv -s -m "not benchmark"

# run all tests (including online and benchmark ones)
[group('test')]
@test-all:
    poetry run pytest tests/ -vv -s

# run test with coverage report (exclude benchmark tests)
[group('test')]
@test-coverage:
    poetry run pytest tests/ -vv -s --cov=src --cov-report=term-missing -m "not benchmark"


# run test files changed since last commit with file watcher, flags can be passed to pytest
[group('test')]
@test-watch *FLAGS:
    # watchexec config details
    # -n: don't spawn another shell for speed
    # -r: restart the process on busy update
    watchexec -nr -w src -w tests -e py --clear -- \
        poetry run pytest tests/ -vv -s --picked \
        --benchmark-columns=mean,median,max,stddev,rounds,iterations \
        --benchmark-sort=mean \
        $FLAGS
