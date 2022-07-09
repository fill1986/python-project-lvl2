#!/usr/bin/env python

import pathlib
import argparse
import json
import yaml
from yaml.loader import SafeLoader

def parser_files(input_file, format = 'json'):
 
    dir_path = pathlib.Path.cwd()
    file_1 = json.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file1.json')))
    file_2 = json.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file2.json')))
    file_3 = yaml.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file1.yaml')), Loader=SafeLoader)
    file_4 = yaml.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file2.yaml')), Loader=SafeLoader)
    # file 5,6 include difficult json
    file_5 = json.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file5.json')))
    file_6 = json.load(open(pathlib.Path(dir_path, 'tests', 'fixtures', 'file6.json')))

    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(input_file)
    elif format == 'json':
        #print('it is json loader')
        return json.loads(input_file)

    #return file_5, file_6
