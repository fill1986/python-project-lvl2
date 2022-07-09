#!/usr/bin/env python

from typing import Callable
#from gendiff_package.parser import parser_files

#file_1, file_2 = parser_files()

def create_tree_node(
    key: str,
    first_dict: dict,
    second_dict: dict
    ):
    first_value = first_dict.get(key)
    second_value = second_dict.get(key)
    
    if key not in second_dict:
        return {'type': 'DELETED', 'name': key, 'value': first_value}
    if key not in first_dict:
        return {'type': 'ADDED', 'name': key, 'value': second_value}
    if isinstance(first_value, dict) and isinstance(second_value, dict):
        #uniq_keys = sorted(first_value.keys() | second_value.keys())
        return {
            'type': 'NESTED',
            'name': key,
            #'children': function(first_value, second_value),
            
            'children': create_AST(first_value, second_value)
        }
    if first_value == second_value:
        return {'type': 'UNCHENGED', 'name': key, 'value': first_value}

    return {
        'type': 'CHANGED',
        'name': key,
        'value_before': first_value,
        'value_after': second_value,
    }

def create_AST(file_first, file_second):
    uniq_keys = sorted(file_first.keys() | file_second.keys())

    ast = map(
        lambda key: create_tree_node(key, file_first, file_second), uniq_keys
    )

    return list(ast)

#print('- - - - -')
#print(create_AST(file_1, file_2))
