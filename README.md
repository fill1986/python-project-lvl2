### Hexlet tests and linter status:
[![Actions Status](https://github.com/fill1986/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/fill1986/python-project-lvl2/actions)
[![Actions Status](https://github.com/fill1986/python-project-lvl2/workflows/linter-check/badge.svg)](https://github.com/fill1986/python-project-lvl2/actions/workflows/linter-check.yaml)
[![Actions Status](https://github.com/fill1986/python-project-lvl2/workflows/pytests/badge.svg)](https://github.com/fill1986/python-project-lvl2/actions/workflows/pytests.yaml)
[![Maintainability](https://api.codeclimate.com/v1/badges/08f54ac62860935c041f/maintainability)](https://codeclimate.com/github/fill1986/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/08f54ac62860935c041f/test_coverage)](https://codeclimate.com/github/fill1986/python-project-lvl2/test_coverage)


### Install and run progtam
Copy files from git and to install:
```
$ git clone https://github.com/fill1986/python-project-lvl2 
$ OurDirectory/
$ cd OurDirectory
$ make install
$ make build
$ make publish
$ make package-install
```

Demonstration installation:

<a href="https://asciinema.org/a/CeCZyqLoh54n71a48HhcCjKrV" target="_blank"><img src="https://asciinema.org/a/CeCZyqLoh54n71a48HhcCjKrV.svg" /></a>


get the difference JSON files
$ gendiff tests/fixtures/first_file.json tests/fixtures/second_file.json

get the difference YAML files
$ gendiff tests/fixtures/first_file.yaml tests/fixtures/second_file.json

get difference by other out formats
$ gendiff --format plain tests/fixtures/first_file.yaml tests/fixtures/second_file.json

$ gendiff --format json tests/fixtures/first_file.yaml tests/fixtures/second_file.json

$ gendiff --format stylish tests/fixtures/first_file.yaml tests/fixtures/second_file.json
