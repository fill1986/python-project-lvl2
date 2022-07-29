import pathlib
import pytest
from gendiff.scripts.gendiff import generate_diff


dir_path = pathlib.Path.cwd()


@pytest.mark.parametrize(
    ('ext_file', 'format_name'),
    [('json', 'stylish'),
     ('yaml', 'stylish'),
     ('json', 'plain'),
     ('yaml', 'plain'),
     ('json', 'json'),
     ('yaml', 'json')]
)
def test_generate_diff(ext_file, format_name):
    first_file = 'tests/fixtures/first_file.{0}'.format(ext_file)
    second_file = 'tests/fixtures/second_file.{0}'.format(ext_file)
    result = generate_diff(first_file, second_file, format_name)
    expected = open(pathlib.Path(dir_path, 'tests', 'fixtures', 'result_{0}.txt'.format(format_name)))

    assert result == expected.read()
    expected.close()
