from gendiff.formaters.stylish import render_stylish
from gendiff.formaters.plain import render_plain
import json


def render(AST, format):
    if format == 'stylish':
        return render_stylish(AST)
    elif format == 'plain':
        return render_plain(AST)
    elif format == 'json':
        return json.dumps(AST)
