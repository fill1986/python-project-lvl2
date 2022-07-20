import json
import yaml

def select_loader(input_data, format):
    if format == 'yaml' or format == 'yml':
        return yaml.safe_load(input_data)
    elif format == 'json':
        return json.loads(input_data)

def parsers(input_data, format='json'):
    return select_loader(input_data, format)
