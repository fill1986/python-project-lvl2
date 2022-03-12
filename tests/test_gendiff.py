import argparse
import json
from gendiff_package.scripts.gendiff import generate_diff


file_1 = json.load(open('/home/evgeny/python-project-lvl2/tests/fixtures/file1.json'))
file_2 = json.load(open('/home/evgeny/python-project-lvl2/tests/fixtures/file2.json'))
result_json = open('/home/evgeny/python-project-lvl2/tests/fixtures/result.txt')


def test_json():
    assert generate_diff(file_1, file_2)  == result_json.read()