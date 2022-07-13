import json
import yaml


def parser_files(input_file, format='json'):

    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(input_file)
    elif format == 'json':
        return json.loads(input_file)
