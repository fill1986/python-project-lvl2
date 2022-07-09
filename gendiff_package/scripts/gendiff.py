#!/usr/bin/env python

#from yaml import parse
#from gendiff_package.parser import parser_files
from gendiff_package.generate_diff import generate_diff

import argparse


'''
# - - - - - - - - 
file_1, file_2 = parser_files()


def generate_diff(file_1, file_2):
    
    result = '{ \n'

    for i in file_1:
        if i in file_2:
            if file_1[i] == file_2[i]:
                result += f'   {i} : {file_1[i]} \n'
            else:
                result += f' - {i} : {file_1[i]} \n'
                result += f' + {i} : {file_2[i]} \n'

        elif i not in file_2:
            result += f' - {i} : {file_1[i]} \n'

    for n in file_2:
        if n not in file_1:
            result += f' + {n} : {file_2[n]} \n'

    return result + '\n' + '}'

#print(generate_diff(file_1, file_2)) # TEMPORY for test
'''
JSON = 'json'
PLAIN = 'plain'
STYLISH = 'stylish'

def main():
    #print('test')
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help = 'set format',
        choices = [STYLISH, PLAIN, JSON],
        default = STYLISH
    )

    args = parser.parse_args()
    #print(generate_diff(args.first_file, args.second_file, args.format))
    #print('test!!!')
    print(generate_diff(args.first_file, args.second_file, args.format))

if __name__ == '__main__':
    main()