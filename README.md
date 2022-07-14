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


### get the difference JSON files
```
$ gendiff tests/fixtures/first_file.json tests/fixtures/second_file.json
```
<a href="https://asciinema.org/a/mhrgvU2YyYzQgV9F0h2yBMf6m" target="_blank"><img src="https://asciinema.org/a/mhrgvU2YyYzQgV9F0h2yBMf6m.svg" /></a>


### get the difference YAML files
```
$ gendiff tests/fixtures/first_file.yaml tests/fixtures/second_file.yaml
```
<a href="https://asciinema.org/a/bvmFiRI2jv3j3tpYXL5DXtMkR" target="_blank"><img src="https://asciinema.org/a/bvmFiRI2jv3j3tpYXL5DXtMkR.svg" /></a>

### get difference by other out formats
```
$ gendiff --format plain tests/fixtures/first_file.json tests/fixtures/second_file.json
```
<a href="https://asciinema.org/a/0n881N0e8wkcvjPkhlnt0FhAt" target="_blank"><img src="https://asciinema.org/a/0n881N0e8wkcvjPkhlnt0FhAt.svg" /></a>


```
$ gendiff --format json tests/fixtures/first_file.json tests/fixtures/second_file.json
```
<a href="https://asciinema.org/a/Hr7eL0gtOLW29gRLwqYMZ2cqx" target="_blank"><img src="https://asciinema.org/a/Hr7eL0gtOLW29gRLwqYMZ2cqx.svg" /></a>


```
$ gendiff --format stylish tests/fixtures/first_file.yaml tests/fixtures/second_file.json
```
<a href="https://asciinema.org/a/ttXxITc9S7EoaxviIqCfjZXKa" target="_blank"><img src="https://asciinema.org/a/ttXxITc9S7EoaxviIqCfjZXKa.svg" /></a>
