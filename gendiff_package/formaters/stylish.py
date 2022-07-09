import itertools





def format_node(
    node_key,
    node_value,
    indent_size: int = 0,
    mark: str = '',
):
    return '{0}{1} {2}: {3}'.format(
        set_indent(indent_size),
        mark,
        node_key,
        stringify(node_value, indent_size),
    )


AST = {'host': {'status': 'no_cnange_value', 'value': 'hexlet.io'}, 'timeout': {'status': 'change_value', 'value': 50}, 'proxy': {'status': 'delete_key', 'value': '123.234.53.22'}, 'follow': {'status': 'delete_key', 'value': False}, 'test_arr_key': {'status': 'change_value', 'value': 256}}
AST2 = {'common': {'status': 'change_value', 'value': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}}, 'group1': {'status': 'change_value', 'value': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}}, 'group2': {'status': 'delete_key', 'value': {'abc': 12345, 'deep': {'id': 45}}}}
AST3  = [{'type': 'NESTED', 'name': 'common', 'children': [{'type': 'ADDED', 'name': 'follow', 'value': False}, {'type': 'UNCHENGED', 'name': 'setting1', 'value': 'Value 1'}, {'type': 'DELETED', 'name': 'setting2', 'value': 200}, {'type': 'CHANGED', 'name': 'setting3', 'value_before': True, 'value_after': None}, {'type': 'ADDED', 'name': 'setting4', 'value': 'blah blah'}, {'type': 'ADDED', 'name': 'setting5', 'value': {'key5': 'value5'}}, {'type': 'NESTED', 'name': 'setting6', 'children': [{'type': 'NESTED', 'name': 'doge', 'children': [{'type': 'CHANGED', 'name': 'wow', 'value_before': '', 'value_after': 'so much'}]}, {'type': 'UNCHENGED', 'name': 'key', 'value': 'value'}, {'type': 'ADDED', 'name': 'ops', 'value': 'vops'}]}]}, {'type': 'NESTED', 'name': 'group1', 'children': [{'type': 'CHANGED', 'name': 'baz', 'value_before': 'bas', 'value_after': 'bars'}, {'type': 'UNCHENGED', 'name': 'foo', 'value': 'bar'}, {'type': 'CHANGED', 'name': 'nest', 'value_before': {'key': 'value'}, 'value_after': 'str'}]}, {'type': 'DELETED', 'name': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'type': 'ADDED', 'name': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]
ast_1 = [{'type': 'NESTED', 'name': 'common', 'children': [{'type': 'ADDED', 'name': 'follow', 'value': False}, {'type': 'UNCHENGED', 'name': 'setting1', 'value': 'Value 1'}, {'type': 'DELETED', 'name': 'setting2', 'value': 200}, {'type': 'CHANGED', 'name': 'setting3', 'value_before': True, 'value_after': None}, {'type': 'ADDED', 'name': 'setting4', 'value': 'blah blah'}, {'type': 'ADDED', 'name': 'setting5', 'value': {'key5': 'value5'}}, {'type': 'NESTED', 'name': 'setting6', 'children': [{'type': 'NESTED', 'name': 'doge', 'children': [{'type': 'CHANGED', 'name': 'wow', 'value_before': '', 'value_after': 'so much'}]}, {'type': 'UNCHENGED', 'name': 'key', 'value': 'value'}, {'type': 'ADDED', 'name': 'ops', 'value': 'vops'}]}]}, {'type': 'NESTED', 'name': 'group1', 'children': [{'type': 'CHANGED', 'name': 'baz', 'value_before': 'bas', 'value_after': 'bars'}, {'type': 'UNCHENGED', 'name': 'foo', 'value': 'bar'}, {'type': 'CHANGED', 'name': 'nest', 'value_before': {'key': 'value'}, 'value_after': 'str'}]}, {'type': 'DELETED', 'name': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'type': 'ADDED', 'name': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

##print(stringify(AST2))
##print(render(AST3))

def set_indent(indent_size: int = 0):
    return '  ' * indent_size

def transform_value_to_str(node_value):
    if isinstance(node_value, bool):
        return str(node_value).lower()
    if node_value is None:
        return 'null'

    return str(node_value)

def stringify(
    node_data,
    indent_size,
):
    if not isinstance(node_data, dict):
        return transform_value_to_str(node_data)

    current_indent = set_indent(indent_size + 1)
    deep_indent_size = indent_size + 2
    deep_indent = set_indent(deep_indent_size + 1)

    processed_data = map(
        lambda data_key, data_value: '{0}{1}: {2}'.format(
            deep_indent,
            data_key,
            stringify(data_value, deep_indent_size),
        ),
        node_data.keys(),
        node_data.values(),
    )
    
    output = itertools.chain(
        '{',
        processed_data,
        ['{0}{1}'.format(current_indent, '}')],
    )

    return '\n'.join(output)

def select_type(node, depth, type, function):
    
    if type == 'NESTED':
        return '  {0}{1}: {2}'.format(
            set_indent(depth),
            node['name'],
            function(node['children'], depth+2),
        )

    elif type == 'ADDED':
        test ='{0}{1} {2}: {3}'.format(set_indent(depth),'+', node['name'], node['value'])
        #print(f'ADDED -    {test}')
        return '{0}{1} {2}: {3}'.format(
            set_indent(depth),
            '+',
            node['name'],
            stringify(node['value'], depth),
        )
    elif type == 'DELETED':
        return '{0}{1} {2}: {3}'.format(
            set_indent(depth),
            '-',
            node['name'],
            stringify(node['value'], depth),
        )
    elif type == 'UNCHENGED':
        return '{0}{1} {2}: {3}'.format(
            set_indent(depth),
            ' ',
            node['name'],
            stringify(node['value'], depth),
        )
    elif type == 'CHANGED':
        return '\n'.join(
            [
                format_node(
                    node['name'],
                    node['value_before'],
                    depth,
                    '-',
                ),
                format_node(
                    node['name'],
                    node['value_after'],
                    depth,
                    '+',
                ),
            ],
        )


    
def render_stylish(value, replacer='-', spaces_count=0):

    def iter_(current_value, depth = 0):
   
        result = map(lambda s_type: select_type(s_type, depth, s_type['type'], iter_), current_value)
        
        return '{{\n{0}\n{1}}}'.format(
            '\n'.join(result),
            set_indent(depth - 1),
        )

        
    
    return iter_(value, 1)

##print(AST3)
#ast_1  = [{'type': 'nested', 'name': 'common', 'children': [{'type': 'added', 'name': 'follow', 'value': False}, {'type': 'unchanged', 'name': 'setting1', 'value': 'Value 1'}, {'type': 'deleted', 'name': 'setting2', 'value': 200}, {'type': 'changed', 'name': 'setting3', 'value_before': True, 'value_after': None}, {'type': 'added', 'name': 'setting4', 'value': 'blah blah'}, {'type': 'added', 'name': 'setting5', 'value': {'key5': 'value5'}}, {'type': 'nested', 'name': 'setting6', 'children': [{'type': 'nested', 'name': 'doge', 'children': [{'type': 'changed', 'name': 'wow', 'value_before': '', 'value_after': 'so much'}]}, {'type': 'unchanged', 'name': 'key', 'value': 'value'}, {'type': 'added', 'name': 'ops', 'value': 'vops'}]}]}, {'type': 'nested', 'name': 'group1', 'children': [{'type': 'changed', 'name': 'baz', 'value_before': 'bas', 'value_after': 'bars'}, {'type': 'unchanged', 'name': 'foo', 'value': 'bar'}, {'type': 'changed', 'name': 'nest', 'value_before': {'key': 'value'}, 'value_after': 'str'}]}, {'type': 'deleted', 'name': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'type': 'added', 'name': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

#print(render_stylish(AST3))
#print(json.dumps(AST3))