#!/usr/bin/env python

import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', default='json', help='set format of output')
parser.add_argument('first_file', default='/home/evgeny/python-project-lvl2/gendiff_package/file1.json')
parser.add_argument('second_file',default='/home/evgeny/python-project-lvl2/gendiff_package/file2.json', help='second file')
args = parser.parse_args()

print(f'args1 {args.first_file}')
print(f'args2 {args.second_file}')

file_1 = json.load(open(args.first_file))
file_2 = json.load(open(args.second_file))

def main():
    #print(file_1)
    #print(file_2)
    def generate_diff(file_1, file_2):
        print(f'file1 {file_1}')
        print(f'file2 {file_2}')
        
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
        
    args = parser.parse_args()

    print(generate_diff(file_1, file_2))


if __name__ == '__main__':
    main()

'''
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
'''