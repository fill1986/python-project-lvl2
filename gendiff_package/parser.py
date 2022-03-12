#!/usr/bin/env python

import argparse
import json

def parser_files():
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--format', default='json', help='set format of output')
    parser.add_argument('first_file', default='/home/evgeny/python-project-lvl2/gendiff_package/file1.json')
    parser.add_argument('second_file',default='/home/evgeny/python-project-lvl2/gendiff_package/file2.json', help='second file')
    args = parser.parse_args()

    file_1 = json.load(open(args.first_file))
    file_2 = json.load(open(args.second_file))
    '''
    file_1 = json.load(open('/home/evgeny/python-project-lvl2/tests/fixtures/file1.json'))
    file_2 = json.load(open('/home/evgeny/python-project-lvl2/tests/fixtures/file2.json'))
    return file_1, file_2


