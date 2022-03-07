install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
gendiff:
	poetry run gendiff '/home/evgeny/python-project-lvl2/gendiff_package/file1.json' '/home/evgeny/python-project-lvl2/gendiff_package/file2.json'
engine:
	poetry run engine '/home/evgeny/python-project-lvl2/gendiff_package/file1.json' '/home/evgeny/python-project-lvl2/gendiff_package/file2.json'
lint:
	poetry run flake8 gendiff_package/


