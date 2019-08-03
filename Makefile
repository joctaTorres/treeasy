.PHONY: test
test:
	pytest . $(PYTEST_OPTIONS)

.PHONY: snapshot-update
snapshot-update: PYTEST_OPTIONS := --snapshot-update
snapshot-update: test

.PHONY: autoflake
autoflake:
	autoflake -r $(AUTOFLAKE_OPTIONS) --exclude */snapshots --remove-unused-variables --remove-all-unused-imports  **/ | tee autoflake.log
	echo "$(AUTOFLAKE_OPTIONS)" | grep -q -- '--in-place' || ! [ -s autoflake.log ]

.PHONY: isort
isort:
	isort -rc **/ --multi-line 3 --trailing-comma --line-width 88 --skip */snapshots $(ISORT_OPTIONS)

.PHONY: black
black:
	black **/ --exclude */snapshots $(BLACK_OPTIONS)

.PHONY: lint
lint: ISORT_OPTIONS := --check-only
lint: BLACK_OPTIONS := --check
lint: autoflake isort black
	mypy **/*.py --ignore-missing-imports
	flake8 ./treeasy

.PHONY: format
format: AUTOFLAKE_OPTIONS := --in-place
format: autoflake isort black