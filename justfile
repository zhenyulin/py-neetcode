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

# ----------------------------------------------------------------------------------- #

#
## SETUP
#

# CONFIG
set ignore-comments
set shell := ["bash", "-uc"] # -u to throw errors for unset variables, -c so that string commands can be run
set windows-shell := ["bash", "-uc"]

# VARS
PYTHONPATH := invocation_directory()
PROJECT_NAME := file_stem(PYTHONPATH)

#
## COMMANDS - DEVELOPMENT
#

# list available commands
[group('dev')]
@default:
    just --list --unsorted

[macos]
@_python:
    pyenv install -s # -s to skip if set python version is already installed

[windows]
@_python:
    VERSION_MATCH="^ *$(pyenv local)" # start with any number of spaces and minor version from .python-version
    PYTHON_VERSION=$(pyenv install --list | grep $VERSION_MATCH | tail -n 1 | xargs) # get the latest patch version
    pyenv install $PYTHON_VERSION -q
    poetry env use $(pyenv which python) # force poetry to use pyenv python on Windows

# install python, dependencies, pre-commit hooks
[group('dev')]
@install:
    echo "using python $(pyenv version-name) ($(which python))"
    just _python
    just lockfile
    poetry install
    poetry run pre-commit install --install-hooks

# remove .venv, tooling cache, test reports, __pycache__
[group('dev')]
[confirm("cleanup .venv and caches? (y/n)")]
cleanup:
    rm -rf .venv/
    rm -rf .**cache**/ # cleanup tooling caches
    rm -rf .coverage
    rm -rf .benchmarks
    rm -rf src/__pycache__ # cleanup pycache
    rm -rf tests/__pycache__ # cleanup pycache
    rm -rf src/**/__pycache__ # cleanup pycache
    rm -rf tests/**/__pycache__ # cleanup pycache

# resolve lockfile conflicts
[group('dev')]
lockfile:
    poetry lock --no-update

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


# run test files changed since last commit with file watcher
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
