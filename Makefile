install:
	poetry install

merge-logs:
	poetry run merge-logs

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=merge_logs --cov-report xml

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 merge_logs tests