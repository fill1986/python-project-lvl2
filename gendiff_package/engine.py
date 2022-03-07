#!/usr/bin/env python

import argparse
#from gendiff_package.scripts.gendiff import generate_diff
#from gendiff_package.scripts import generate_diff
from gendiff_package.scripts import generate_diff
import json


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', default='json', help='set format of output')
parser.add_argument('first_file', default='/home/evgeny/python-project-lvl2/gendiff_package/file1.json')
parser.add_argument('second_file',default='/home/evgeny/python-project-lvl2/gendiff_package/file2.json', help='second file')
args = parser.parse_args()

file_1 = json.load(open(args.first_file))
file_2 = json.load(open(args.second_file))


def main():
    print('test')
    #generate_diff(file_1, file_2)


if __name__ == '__main__':
    main()

