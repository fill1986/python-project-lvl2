from gendiff.create_AST import create_AST
from gendiff.parsers import parsers
import os
from gendiff.formaters.render import render


def read_file(path):
    with open(path) as filename:
        _, extension = os.path.splitext(path)
        return filename.read(), extension[1:]


def generate_diff(first_file, second_file, format_name='stylish'):
    readed_first_file, ext_first_file = read_file(first_file)
    first = parsers(readed_first_file, ext_first_file)

    readed_second_file, ext_second_file = read_file(second_file)
    second = parsers(readed_second_file, ext_second_file)

    AST = create_AST(first, second)

    return render(AST, format_name)
