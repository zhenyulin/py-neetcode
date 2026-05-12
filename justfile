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
# FEATURES
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

### VARIABLES
PYTHONPATH := invocation_directory()
PROJECT_NAME := file_stem(PYTHONPATH)
LOCAL_TEST_SCOPE := "not complex and not benchmark and not online"
WHEEL_CACHE_DIR := "/var/folders/pl/"
CONFIG_FILE_PATTERNS := ".editorconfig .coveragerc .git* .python-version* *.yaml *.yml *.ini *.toml"
CONFIG_FILE_EXCLUDES := "pyproject.toml"

### default recipe #keep on top

# list available commands
@list:
    just --list --unsorted

#
#   RECIPE GROUP - DEVELOPMENT
#

### Install

# install python, create .env, install deps & pre-commit hooks
[group('dev')]
@install:
    uv python install
    just env
    uv lock --upgrade
    uv sync
    uv pip install -e ./cython
    uv pip install -e ./rust
    uv run pre-commit install --install-hooks # --install-hooks setup pre-commit cache
    uv run nbstripout --install --python .venv/bin/python

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
    perl -0pi -e "s/target-version = \"py[0-9]{2,3}\"/target-version = \"${short}\"/g" ruff.toml

# create the default .env from template and cache, -f to create new .env file
[group('dev')]
@env *FLAGS:
    # remove existing .env file if -f is set
    if [ "$FLAGS" = "-f" ]; then rm -f .env; fi; \
    if [ -f ".env" ]; then echo "existing .env found:"; cat .env; else \
        cp .env-template .env; echo "" >> .env; \
        if [ -f ".env-cache" ]; then cat .env-cache >> .env; fi; \
        just _use_last_key_value .env; \
        echo "new .env created:"; \
        sort .env -o .env; \
        cat .env; \
    fi

### Cleanup

# remove .venv, python & tooling cache, test reports; -a to remove .env, run & test output
[confirm("cleanup .venv, build & tooling caches? (y/n)")]
[group('dev')]
cleanup *FLAGS:
    if [ "$FLAGS" == "-a" ]; then \
        -uv run nbstripout --uninstall; \
        -uv run pre-commit uninstall; \
        just _cleanup_test_report; \
        just _cleanup_output; \
        rm -f .env; \
    fi; \
    just _cleanup_tooling_cache
    just _cleanup_pycache
    just _cleanup_cython
    just _cleanup_rust
    rm -rf .venv/

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

## RECIPE GROUP - CREDENTIALS

# TODO
@_fetch_credentials:
    echo "fetching credentials from remote sources"

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
    watchexec -nr -w src -w tests -e py -w "$WHEEL_CACHE_DIR" -e whl --clear -- \
        uv run pytest tests/ -vv -s -m "$SCOPE" --picked \
        --cov=src \
        --cov-report=term-missing \
        --benchmark-columns=mean,median,max,stddev,rounds,iterations \
        --benchmark-sort=mean \
        --benchmark-max-time=1 \
        --benchmark-save=run \
        --benchmark-compare

#
#   RECIPE GROUP - Docker
#

# build the docker image
[group('docker')]
@docker-build:
    uv lock
    just _cleanup_pycache
    docker build --build-arg PYTHON_VERSION=$(cat .python-version) -t $PROJECT_NAME .

# run the docker image, cli arguments can be passed, container /output is mounted to ./output
[group('docker')]
@docker-run *PARAMETERS:
    docker run --env-file .env -v ./output:/output $PROJECT_NAME python -m src $PARAMETERS

# run the tests in docker image
[group('docker')]
@docker-test SCOPE=LOCAL_TEST_SCOPE:
    docker run --env-file .env $PROJECT_NAME pytest tests/ -vv -s -m "$SCOPE"

#
#   RECIPE GROUP - Cython
#

# build cython script
[group('cython')]
@cython-build:
    cd cython && uv pip install -e .

# run cython-lint
[group('cython')]
@cython-check:
    -uv run cython-lint cython --max-line-length 110

@_cleanup_cython:
    rm -rf cython/*.egg-info
    rm -rf cython/build
    find cython -name '*.c'   -delete
    find cython -name '*.so'  -delete
    find cython -name '*.pyd' -delete
    rm -rf build/

#
#   RECIPE GROUP - Rust
#

# build rust script
[group('rust')]
@rust-build:
    RUSTFLAGS="-C target-cpu=native" \
    maturin develop --release --strip --manifest-path=rust/Cargo.toml

[group('rust')]
@rust-build-watch:
    watchexec -n -r -w rust/src -e rs --clear -- \
        just rust-build

@_cleanup_rust:
    rm -rf rust/target/

#
#   RECIPE GROUP - Template
#

@_set_project_name:
    template_name=$(basename $CONFIG_TEMPLATE_PATH)
    sed -i "s|${template_name}|${PROJECT_NAME}|g" pyproject.toml

# remove all the template files when init a repo
[group('template')]
@_init:
    find src ! -name "__init__.py" -mindepth 1 -delete
    find tests ! -name "__init__.py" -mindepth 1 -delete
    rm README.md && echo "# $PROJECT_NAME" > README.md
    just _set_project_name

@_template_repo_sync:
    echo "sync config repo to origin/main"
    git -C $CONFIG_TEMPLATE_PATH checkout -q main
    git -C $CONFIG_TEMPLATE_PATH pull -q

@_copy_template_config_files DESTINATION='_config':
    mkdir -p "$DESTINATION"; \
    exclude_args=""; \
    for e in {{CONFIG_FILE_EXCLUDES}}; do exclude_args="$exclude_args ! -name $e"; done; \
    set -f; \
    for p in {{CONFIG_FILE_PATTERNS}}; do \
        find "$CONFIG_TEMPLATE_PATH" -maxdepth 1 -type f -iname "$p" $exclude_args -exec cp -p {} "$DESTINATION/" \; ; \
    done

@_strip_repo_specific_config DIR='_config':
    START_MARK="# \* <- repo specific config start:"; \
    END_MARK="# \* repo specific config end ->"; \
    find "$DIR" -maxdepth 1 -type f -print0 | \
    while IFS= read -r -d '' file; do \
        echo "stripping $file"; \
        sed -e "/${START_MARK}/,/${END_MARK}/d" "$file" > "$file.tmp" && mv "$file.tmp" "$file"; \
    done

@_reserve_repo_specific_config RESERVE_DIR='_config_reserve':
    START_MARK="# \* <- repo specific config start:"; \
    END_MARK="# \* repo specific config end ->"; \
    mkdir -p "$RESERVE_DIR"; \
    find . -maxdepth 1 -type f -print0 | \
    while IFS= read -r -d '' file; do \
        filename=$(basename "$file"); \
        if grep -q "$START_MARK" "$file" 2>/dev/null; then \
            echo "reserving repo specific config from $file"; \
            sed -n "/${START_MARK}/,/${END_MARK}/p" "$file" > "$RESERVE_DIR/$filename"; \
        fi; \
    done

@_restore_repo_specific_config RESERVE_DIR='_config_reserve' TARGET_DIR='_config':
    find "$RESERVE_DIR" -maxdepth 1 -type f -print0 | \
    while IFS= read -r -d '' file; do \
        filename=$(basename "$file"); \
        if [ -f "$TARGET_DIR/$filename" ]; then \
            echo "restoring repo specific config to $TARGET_DIR/$filename"; \
            cat "$file" >> "$TARGET_DIR/$filename"; \
        fi; \
    done; \
    rm -rf "$RESERVE_DIR"

@_reconcile_cspell DIR='_config':
    cat cspell.config.yaml >> "$DIR"/cspell.config.yaml
    just _use_first_occurrence "$DIR"/cspell.config.yaml

# copy the latest config files from CONFIG_TEMPLATE_PATH#main
[group('template')]
@config:
    just _template_repo_sync

    echo "coping config files from $CONFIG_TEMPLATE_PATH"
    -cp -r $CONFIG_TEMPLATE_PATH/.vscode .
    just _reserve_repo_specific_config _config_reserve
    just _copy_template_config_files _config
    just _strip_repo_specific_config _config
    just _restore_repo_specific_config _config_reserve _config

    echo "reconcile local config with template config"
    just _reconcile_cspell
    cp -a _config/. .
    rm -rf _config

# copy the latest shared lib from CONFIG_TEMPLATE_PATH#main
[group('template')]
@shared:
    echo "coping /shared from $CONFIG_TEMPLATE_PATH"
    just _template_repo_sync
    rm -rf ./src/shared
    cp -r $CONFIG_TEMPLATE_PATH/src/shared ./src


## UTILITY RECIPES

# keep the last occurrence of each line in the file, drop empty lines
@_use_last_key_value file:
    # -F= use = as the separator, NF checks for non-empty lines
    # $1 is the key name before =, $0 is the whole line, stored in an associative array `lines`
    awk -F= 'NF && $1 {lines[$1] = $0} END {for (key in lines) print lines[key]}' {{file}} > {{file}}.tmp
    mv {{file}}.tmp {{file}}

# keep the first occurrence of each line in the file, drop empty lines
@_use_first_occurrence file:
    # -F= use = as the separator, NF checks for non-empty lines
    # $1 is the key name before =, $0 is the whole line, stored in an associative array `lines`
    awk '!seen[$0]++ {print}' {{file}} > {{file}}.tmp
    mv {{file}}.tmp {{file}}
