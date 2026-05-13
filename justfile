# LINKS
#
# justfile docs: https://just.systems/man/en/
# cheat sheet: https://cheatography.com/linux-china/cheat-sheets/justfile/
#
# FUNCTIONS
#
# justfile functions are preferred over shell functions for cross-platform compatibility
# justfile function docs: https://just.systems/man/en/chapter_31.html
#
# NOTABLE FEATURES
#
# - prepend hyphen to command to ignore errors: https://just.systems/man/en/chapter_30.html
#   e.g. `-rm .env` wouldn't throw error if .env file doesn't exist
#
# - variadic parameters *PARAMETERS accepts zero ro more arguments, passing them as string
#   e.g. *FLAGS, *PARAMETERS, $FLAGS, $PARAMETERS to access
#
# CAVEATS - DIFFERENT SYNTAXES INSIDE/OUTSIDE RECIPE
#
#  - outside recipe: just syntax, e.g. `PROJECT_NAME := file_stem(PYTHONPATH)` [referenced by VAR_NAME]
#  - inside recipe: shell syntax, e.g. `ipykernel install --name $PROJECT_NAME` [referenced by $VAR_NAME]
#    - inside recipe, use "$VAR_NAME" to interpolate strings correctly
#
# CAVEATS - RECIPE NAME
#
# - recipe name with leading underscore `_` is private, e.g. `@_env_clean` is not listed in `just --list`
# - recipe name can't start with a dot, e.g. `@.env` is not valid
#
# -----------------------------------------------------------------------------------------------
#
#   SETUP
#
### CONFIG

set ignore-comments := true

# load .env file

set dotenv-load := true

# export env variables

set export := true

# -u to throw errors for unset variables
# -c so that string commands can be run

set shell := ["bash", "-uc"]
set windows-shell := ["bash", "-uc"]

### CONSTANTS

PYTHONPATH := invocation_directory()
PROJECT_NAME := file_stem(PYTHONPATH)

# template config values

ESSENTIAL_TEMPLATE_FILES := ".vscode, .config-template, justfile, .editorconfig, .pre-commit-config.yaml, cspell.config.yaml, .coveragerc, .gitattributes, .gitignore, .python-version, Dockerfile, pyrightconfig.json, pytest.ini, ruff.toml"
REPO_CONFIG_DIR := "_repo_config"
TEMPLATE_CONFIG_DIR := "_config"

### VARIABLES

LOCAL_TEST_SCOPE := "not complex and not benchmark and not online"

#
#   DEFAULT RECIPE [keep on top]
#

# list available commands
@list:
    just --list --unsorted

#
#   RECIPE GROUP - DEVELOPMENT
#
### Install

# install python, create .config & .env, install deps & pre-commit hooks
[group('dev')]
@install:
    uv python install
    just config
    just env
    uv lock --upgrade
    uv sync
    uv run pre-commit install --install-hooks # --install-hooks setup pre-commit cache
    uv run nbstripout --install --python .venv/bin/python

### Python Version

# update python version across config files
[group('dev')]
@python-version VERSION:
    if [ -z "$VERSION" ]; then echo "usage: just python-version <major.minor[.patch]>"; exit 1; fi; \
    major="$(echo "$VERSION" | cut -d. -f1)"; \
    minor="$(echo "$VERSION" | cut -d. -f2)"; \
    if [ -z "$major" ] || [ -z "$minor" ]; then echo "invalid version: $VERSION"; exit 1; fi; \
    short="py${major}${minor}"; \
    echo "$VERSION" > .python-version; \
    perl -0pi -e "s/requires-python = \">=[0-9]+\\.[0-9]+(?:\\.[0-9]+)?\"/requires-python = \">=${VERSION}\"/g" pyproject.toml; \
    perl -0pi -e "s/target-version = \"py[0-9]{2,3}\"/target-version = \"${short}\"/g" ruff.toml; \
    perl -0pi -e "s/(name: pythonVersion\\n    value: )\"[0-9]+\\.[0-9]+(?:\\.[0-9]+)?\"/\\1\"${VERSION}\"/" .ado/azure-container-pipeline.yml; \
    perl -0pi -e "s/(name: PYTHON_VERSION\\n    value: )\"[0-9]+\\.[0-9]+(?:\\.[0-9]+)?\"/\\1\"${VERSION}\"/" .ado/azure-function-pipeline.yml

### .Config

# create the default .config from template, -f to create new .config file
[group('dev')]
@config *FLAGS:
    if [ "$FLAGS" = "-f" ]; then rm -f .config; fi; \
    if [ -f ".config" ]; then echo "existing .config found:"; cat .config; else \
        cp .config-template .config; \
        if [ -f ".config-cache" ]; then cat .config-cache >> .config; fi; \
        just _use_last_key_value .config; \
        echo "new .config created:"; \
        sort .config -o .config; \
        cat .config; \
    fi

### .Env

# create the default .env from template, -f to create new .env file
[group('dev')]
@env *FLAGS:
    if [ "$FLAGS" = "-f" ]; then rm -f .env; fi; \
    if [ -f ".env" ]; then echo "existing .env found:"; cat .env; else \
        cp .env-template .env; \
        echo "PROJECT_NAME=$PROJECT_NAME" >> .env; \
        just _env_kv_pull; \
        if [ -f ".env-cache" ]; then cat .env-cache >> .env; fi; \
        just _use_last_key_value .env; \
        echo "new .env created:"; \
        sort .env -o .env; \
        cat .env; \
    fi

### HELPER GROUP - .Env

# pull secrets from Azure Key Vault listed in .env-kv and append to env
@_env_kv_pull:
    export KV_NAME="$(awk -F= '/^CONFIG_AZURE_KEYVAULT_NAME=/{print $2}' .config)"; \
    if [ -z "$KV_NAME" ]; then \
        echo "skipping pulling secrets from Azure Key Vault, as CONFIG_AZURE_KEYVAULT_NAME not set"; \
        exit 0; \
    fi; \
    bash .scripts/env-kv-pull.sh

### Cleanup

# remove .venv, python & tooling cache, test reports; -a to remove .env, run & test output
[confirm("cleanup .venv, build & tooling caches? (y/n)")]
[group('dev')]
@cleanup *FLAGS:
    if [ "$FLAGS" == "-a" ]; then \
        uv run nbstripout --uninstall || true; \
        uv run pre-commit uninstall || true; \
        just _cleanup_test_report; \
        just _cleanup_output; \
        rm -f .env; \
    fi; \
    just _cleanup_tooling_cache
    just _cleanup_pycache
    just _cleanup_cython
    just _cleanup_rust
    rm -rf .venv/

### HELPER GROUP - Cleanup

@_cleanup_output:
    rm -rf output/**
    touch output/.gitkeep

@_cleanup_test_report:
    rm -rf .benchmarks/
    rm -rf .coverage
    rm -rf .coverage.*
    rm -rf report/

@_cleanup_tooling_cache:
    rm -rf .pytest_cache
    rm -rf .ruff_cache

# bash doesn't support recursive ** resolution
@_cleanup_pycache:
    rm -rf src/__pycache__
    rm -rf src/**/__pycache__
    rm -rf tests/__pycache__
    rm -rf tests/**/__pycache__

@_cleanup_cython:
    rm -rf src/**/*.c
    rm -rf src/**/*.so
    rm -rf src/**/*.pyd
    rm -rf build/

@_cleanup_rust:
    rm -rf rust/target/

#
#   RECIPE GROUP - Code Quality
#

# run code quality checks
[group('quality')]
@check:
    just format lint type-check

# run code quality checks with file watcher
[group('quality')]
@check-watch:
    watchexec -n -r -w src -w tests -w pyrightconfig.json -w ruff.toml --clear -- just check

# format code using ruff
[group('quality')]
@format:
    uv run ruff format src tests

# lint code using ruff
[group('quality')]
@lint:
    uv run ruff check src tests --fix

# run pyright type checks
[group('quality')]
@type-check:
    uv run pyright

# run pre-commit hooks manually
[group('quality')]
@pre-commit:
    uv run pre-commit run --hook-stage pre-commit

# run pre-push hooks manually
[group('quality')]
@pre-push:
    uv run pre-commit run --hook-stage pre-push

#
#   RECIPE GROUP - Test
#

# run the src as a module, cli arguments can be passed
[group('test')]
@run *PARAMETERS:
    uv run dotenv run -- python -m src $PARAMETERS

# run test cases with scope
[group('test')]
@test SCOPE=LOCAL_TEST_SCOPE:
    uv run pytest tests/ -vv -s -m "$SCOPE"

# run test coverage with scope
[group('test')]
@test-coverage SCOPE=LOCAL_TEST_SCOPE:
    uv run pytest tests/ -vv -s -m "$SCOPE" --cov=src --cov-report=term-missing

# run test on changed files with scope
[group('test')]
@test-watch SCOPE=LOCAL_TEST_SCOPE:
    # watchexec config details
    # -n: don't spawn another shell for speed
    # -r: restart the process on busy update
    watchexec -nr -w src -w tests -e py --clear -- \
        uv run pytest tests/ -vv -s -m "$SCOPE" --picked \
        --cov=src \
        --cov-report=term-missing \
        --benchmark-columns=mean,median,max,stddev,rounds,iterations \
        --benchmark-sort=mean \

#
#   RECIPE GROUP - Docker
#

# build the docker image (runtime|test)
[group('docker')]
@docker-build:
    uv lock
    just _cleanup_pycache
    docker build \
        --build-arg PYTHON_VERSION="$(cat .python-version)" \
        --tag $PROJECT_NAME \
        .

# run the docker image, cli arguments can be passed, container /output is mounted to ./output
[group('docker')]
@docker-run *PARAMETERS:
    docker run --env-file .env -v ./output:/output $PROJECT_NAME python -m src $PARAMETERS

# run the tests in docker image
[group('docker')]
@docker-test SCOPE=LOCAL_TEST_SCOPE:
    docker run --env-file .env ${PROJECT_NAME}-test pytest tests/ -vv -s -m "$SCOPE"

#
#   RECIPE GROUP - Cython
#

# build cython script
[group('cython')]
@cython-build:
    uv run python setup.py build_ext --inplace

# run cython-lint
[group('cython')]
@cython-check:
    -uv run cython-lint src --max-line-length 110

#
#   RECIPE GROUP - Rust
#

# build rust script
[group('rust')]
@rust-build:
    maturin develop --manifest-path=rust/Cargo.toml

#
#   RECIPE GROUP - Template
#
### INIT

# init a new repo from the template
[group('template')]
@init:
    find src ! -name "__init__.py" -mindepth 1 -delete
    find tests ! -name "__init__.py" -mindepth 1 -delete
    rm README.md && echo "# $PROJECT_NAME" > README.md
    just _set_project_name

### HELPER GROUP - Init

# resolve CONFIG_TEMPLATE_PATH from .config
@_get_config_template_path:
    if [ ! -f ".config" ]; then \
        echo ".config not found"; \
        exit 1; \
    fi; \
    config_path="$(awk -F= '/^CONFIG_TEMPLATE_PATH=/{print $2}' .config)"; \
    if [ -z "$config_path" ]; then \
        echo "CONFIG_TEMPLATE_PATH is empty in .config"; \
        exit 1; \
    fi; \
    echo "$config_path"

@_set_project_name:
    config_path="$(just _get_config_template_path)"; \
    template_name="$(basename "$config_path")"; \
    sed -i "s|${template_name}|${PROJECT_NAME}|g" pyproject.toml

### Config, Shared

# copy the latest config files from CONFIG_TEMPLATE_PATH#main
[group('template')]
@template:
    just _template_repo_sync

    config_path="$(just _get_config_template_path)"; \
    echo "coping config files from $config_path"; \
    cp -r "$config_path"/.vscode . || true
    just _reserve_repo_specific_config
    just _copy_template_config_files _config
    just _strip_repo_specific_config _config
    just _restore_repo_specific_config _config

    echo "reconcile local config with template config"
    just _reconcile_cspell
    cp -a "$TEMPLATE_CONFIG_DIR"/. .
    rm -rf "$TEMPLATE_CONFIG_DIR"
    rm -rf "$REPO_CONFIG_DIR"

# copy the latest shared lib from CONFIG_TEMPLATE_PATH#main
[group('template')]
@shared:
    config_path="$(just _get_config_template_path)"; \
    echo "coping /shared from $config_path"; \
    just _template_repo_sync; \
    rm -rf ./src/shared; \
    cp -r "$config_path"/src/shared ./src

### HELPER GROUP - Config, Shared

@_template_repo_sync:
    config_path="$(just _get_config_template_path)"; \
    echo "sync config repo to origin/main"; \
    git -C "$config_path" checkout -q main; \
    git -C "$config_path" pull -q

@_copy_template_config_files DESTINATION=TEMPLATE_CONFIG_DIR:
    config_path="$(just _get_config_template_path)"; \
    extras="$(grep '^CONFIG_TEMPLATE_FILE_EXTRAS=' .config | sed 's/^[^=]*=//' | tr -d \"\")"; \
    mkdir -p "$DESTINATION"; \
    combined="$(printf '%s,%s' "$ESSENTIAL_TEMPLATE_FILES" "$extras")"; \
    excluded="$(echo "$combined" | tr ',' '\n' | sed 's/^ *//' | grep '^-' | sed 's/^-//')"; \
    echo "$combined" | tr ',' '\n' | sed 's/^ *//' | grep -v '^-' | grep -v '^$' | \
    while IFS= read -r f; do \
        echo "$excluded" | grep -qxF "$f" && continue; \
        [ -e "$config_path/$f" ] && cp -rp "$config_path/$f" "$DESTINATION/"; \
    done

@_reserve_repo_specific_config DEST=REPO_CONFIG_DIR:
    START_MARK="# \* <- repo specific config start:"; \
    END_MARK="# \* repo specific config end ->"; \
    mkdir -p "$DEST"; \
    find . -maxdepth 1 -type f \
        ! -name "*.json" ! -name "*.yml" ! -name "*.yaml" ! -name "*.toml" ! -name "*.ini" \
        -print0 | \
    while IFS= read -r -d '' file; do \
        filename=$(basename "$file"); \
        if grep -q "$START_MARK" "$file" 2>/dev/null; then \
            echo "reserving repo specific config from $file"; \
            sed -n "/${START_MARK}/,/${END_MARK}/p" "$file" > "$DEST/$filename"; \
        fi; \
    done

@_strip_repo_specific_config DIR=TEMPLATE_CONFIG_DIR:
    START_MARK="# \* <- repo specific config start:"; \
    END_MARK="# \* repo specific config end ->"; \
    find "$DIR" -maxdepth 1 -type f -print0 | \
    while IFS= read -r -d '' file; do \
        echo "stripping $file"; \
        sed "/${START_MARK}/,/${END_MARK}/d" "$file" > "$file.tmp" && mv "$file.tmp" "$file"; \
    done

@_restore_repo_specific_config DIR=TEMPLATE_CONFIG_DIR:
    if [ ! -d "$REPO_CONFIG_DIR" ]; then exit 0; fi; \
    find "$REPO_CONFIG_DIR" -maxdepth 1 -type f -print0 | \
    while IFS= read -r -d '' reserved; do \
        target="$DIR/$(basename "$reserved")"; \
        if [ -f "$target" ]; then \
            echo "restoring repo specific config to $target"; \
            printf '\n' >> "$target"; \
            cat "$reserved" >> "$target"; \
        fi; \
    done

@_reconcile_cspell DIR=TEMPLATE_CONFIG_DIR:
    cat cspell.config.yaml >> "$DIR"/cspell.config.yaml
    just _use_first_occurrence "$DIR"/cspell.config.yaml
    file="$DIR/cspell.config.yaml"; \
    { head -3 "$file"; tail -n +4 "$file" | sort -f; } > "$file.tmp" && mv "$file.tmp" "$file"

#
# UTILITY RECIPES
#

# keep the last occurrence of each line in the file, drop empty lines
@_use_last_key_value file:
    # -F= use = as the separator, NF checks for non-empty lines
    # $1 is the key name before =, $0 is the whole line, stored in an associative array `lines`
    awk -F= 'NF && $1 {lines[$1] = $0} END {for (key in lines) print lines[key]}' {{ file }} > {{ file }}.tmp
    mv {{ file }}.tmp {{ file }}

# keep the first occurrence of each line in the file, drop empty lines
@_use_first_occurrence file:
    # -F= use = as the separator, NF checks for non-empty lines
    # $1 is the key name before =, $0 is the whole line, stored in an associative array `lines`
    awk '!seen[$0]++ {print}' {{ file }} > {{ file }}.tmp
    mv {{ file }}.tmp {{ file }}
