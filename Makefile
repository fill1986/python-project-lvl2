install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
gendiff:
	poetry run gendiff '/home/evgeny/python-project-lvl2/tests/fixtures/file5.json' '/home/evgeny/python-project-lvl2/tests/fixtures/file6.json'
gendiff_yaml:
	poetry run gendiff '/home/evgeny/python-project-lvl2/tests/fixtures/file1.yaml' '/home/evgeny/python-project-lvl2/tests/fixtures/file1.yaml'
test:
	poetry run pytest
lint:
	poetry run flake8 gendiff_package/
test-coverage:
	poetry run pytest --cov -vv --cov-report xml




