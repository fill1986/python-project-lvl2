#!/usr/bin/env python

from gendiff_package.parser import parser_files

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

print(generate_diff(file_1, file_2)) # TEMPORY for test

def main():
    print('test')

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