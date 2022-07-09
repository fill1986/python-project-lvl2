from gendiff_package.create_AST import create_AST
from gendiff_package.parser import parser_files
import os
from gendiff_package.formaters.render import render


def read_file(path):
    with open(path) as filename:
        _, extension = os.path.splitext(path)
        return filename.read(), extension[1:]

def generate_diff(first_file, second_file, format_name = 'stylish'):
    #print(read_file(first_file))
    #print('!!!!!!!!!!!!!!!')
    
    #print(parser_files(read_file(first_file)))

    readed_first_file, ext_first_file = read_file(first_file)
    first = parser_files(readed_first_file, ext_first_file)

    readed_second_file, ext_second_file = read_file(second_file)
    second = parser_files(readed_second_file, ext_second_file)

    AST = create_AST(first,second) 

    #print(f'first_file - {first_file}')
    #print(f'format - {format_name}')

    return render(AST, format_name)