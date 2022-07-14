import pathlib
from yaml.loader import SafeLoader
from gendiff_package.scripts.gendiff import generate_diff

'''
dir_path = pathlib.Path.cwd()
file_1 = json.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file1.json')))
file_2 = json.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file2.json')))
result_stylish_simple = open(pathlib.Path(dir_path, 'tests', 'fixtures', 'result.txt'))
file_3 = yaml.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file1.yaml')), Loader=SafeLoader)
file_4 = yaml.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file2.yaml')), Loader=SafeLoader)
result = result_stylish_simple.read()
'''

dir_path = pathlib.Path.cwd()
result_stylish_simple = (open(pathlib.Path(dir_path, 'tests', 'fixtures', 'result.txt'))).read()
result_stylish_simple_nested = (open(pathlib.Path(dir_path, 'tests', 'fixtures', 'result_sylish_nested_json.txt'))).read()
result_plain_format = (open(pathlib.Path(dir_path, 'tests', 'fixtures', 'result_plain_format.txt'))).read()
result_json_format = (open(pathlib.Path(dir_path, 'tests', 'fixtures', 'result_json_format.txt'))).read()


#print(result)
#print(generate_diff(file_1, file_2, 'stylish'))

#print(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
#print(result)


def test_stylish_simple_json_files():
    assert generate_diff('tests/fixtures/first_file.json', 'tests/fixtures/second_file.json') == result_stylish_simple

def test_stylish_nested_json_files():
    assert generate_diff('tests/fixtures/first_file_nested.json', 'tests/fixtures/second_file_nested.json') == result_stylish_simple_nested

def test_stylish_yaml_files():
    assert generate_diff('tests/fixtures/first_file_nested.yaml', 'tests/fixtures/second_file_nested.yaml') == result_stylish_simple_nested

def test_plain_format():
    assert generate_diff('tests/fixtures/first_file_nested.json', 'tests/fixtures/second_file_nested.json', 'plain') == result_plain_format

def test_json_format():
    assert generate_diff('tests/fixtures/first_file_nested.json', 'tests/fixtures/second_file_nested.json', 'json') == result_json_format

