install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
gendiff:
	poetry run gendiff '/home/evgeny/python-project-lvl2/tests/fixtures/first_file.json' '/home/evgeny/python-project-lvl2/tests/fixtures/second_file.json'
gendiff_yaml:
	poetry run gendiff '/home/evgeny/python-project-lvl2/tests/fixtures/first_file.yaml' '/home/evgeny/python-project-lvl2/tests/fixtures/second_file.yaml'
test:
	poetry run pytest
lint:
	poetry run flake8 gendiff_package/
test-coverage:
	poetry run pytest --cov -vv --cov-report xml




