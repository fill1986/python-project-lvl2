import pathlib
import json
from gendiff_package.scripts.gendiff import generate_diff

dir_path = pathlib.Path.cwd()
file_1 = json.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file1.json')))
file_2 = json.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file2.json')))
result_json = open(pathlib.Path(dir_path, 'tests', 'fixtures', 'result.txt'))


def test_json():
    assert generate_diff(file_1, file_2)  == result_json.read()