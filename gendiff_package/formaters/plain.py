
def transform_value_to_str(node_value):
    """Transfom input values to string."""
    if isinstance(node_value, bool):
        return str(node_value).lower()
    if node_value is None:
        return 'null'

    return str(node_value)

def stringify(node_data):
    """Stringify data."""
    if isinstance(node_data, str):
        return "'{0}'".format(node_data)

    return (
        '[complex value]'
        if isinstance(node_data, dict)
        else transform_value_to_str(node_data)
    )




def select_type_add_return_str(node, parent, function):
    if node['type'] == 'ADDED':
        return f"Property '{parent}{node['name']}' was added with value: {stringify(node['value'])}"
    elif node['type'] == 'CHANGED':
        return f"Property '{parent}{node['name']}' was updated. From {stringify(node['value_before'])} to {stringify(node['value_after'])}"
    elif node['type'] == 'DELETED':
        return f"Property '{parent}{node['name']}' was removed"
    elif node['type'] == 'NESTED':
        return function(node['children'],f"{parent}{node['name']}.")
    elif node['type'] == 'UNCHENGED':
        #print('')
        #return f"unchanged"
        return f''



ast_test = [{'type': 'DELETED', 'name': 'follow', 'value': False}, {'type': 'UNCHENGED', 'name': 'host', 'value': 'hexlet.io'}, {'type': 'DELETED', 'name': 'proxy', 'value': '123.234.53.22'}, {'type': 'CHANGED', 'name': 'timeout', 'value_before': 50, 'value_after': 20}, {'type': 'ADDED', 'name': 'verbose', 'value': True}]
ast_1  = [{'type': 'nested', 'name': 'common', 'children': [{'type': 'added', 'name': 'follow', 'value': False}, {'type': 'unchanged', 'name': 'setting1', 'value': 'Value 1'}, {'type': 'deleted', 'name': 'setting2', 'value': 200}, {'type': 'changed', 'name': 'setting3', 'value_before': True, 'value_after': None}, {'type': 'added', 'name': 'setting4', 'value': 'blah blah'}, {'type': 'added', 'name': 'setting5', 'value': {'key5': 'value5'}}, {'type': 'nested', 'name': 'setting6', 'children': [{'type': 'nested', 'name': 'doge', 'children': [{'type': 'changed', 'name': 'wow', 'value_before': '', 'value_after': 'so much'}]}, {'type': 'unchanged', 'name': 'key', 'value': 'value'}, {'type': 'added', 'name': 'ops', 'value': 'vops'}]}]}, {'type': 'nested', 'name': 'group1', 'children': [{'type': 'changed', 'name': 'baz', 'value_before': 'bas', 'value_after': 'bars'}, {'type': 'unchanged', 'name': 'foo', 'value': 'bar'}, {'type': 'changed', 'name': 'nest', 'value_before': {'key': 'value'}, 'value_after': 'str'}]}, {'type': 'deleted', 'name': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'type': 'added', 'name': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]
ast_test2 = [{'type': 'NESTED', 'name': 'common', 'children': [{'type': 'ADDED', 'name': 'follow', 'value': False}, {'type': 'UNCHENGED', 'name': 'setting1', 'value': 'Value 1'}, {'type': 'DELETED', 'name': 'setting2', 'value': 200}, {'type': 'CHANGED', 'name': 'setting3', 'value_before': True, 'value_after': None}, {'type': 'ADDED', 'name': 'setting4', 'value': 'blah blah'}, {'type': 'ADDED', 'name': 'setting5', 'value': {'key5': 'value5'}}, {'type': 'NESTED', 'name': 'setting6', 'children': [{'type': 'NESTED', 'name': 'doge', 'children': [{'type': 'CHANGED', 'name': 'wow', 'value_before': '', 'value_after': 'so much'}]}, {'type': 'UNCHENGED', 'name': 'key', 'value': 'value'}, {'type': 'ADDED', 'name': 'ops', 'value': 'vops'}]}]}, {'type': 'NESTED', 'name': 'group1', 'children': [{'type': 'CHANGED', 'name': 'baz', 'value_before': 'bas', 'value_after': 'bars'}, {'type': 'UNCHENGED', 'name': 'foo', 'value': 'bar'}, {'type': 'CHANGED', 'name': 'nest', 'value_before': {'key': 'value'}, 'value_after': 'str'}]}, {'type': 'DELETED', 'name': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'type': 'ADDED', 'name': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

def filter_AST_for_plain_format(type_obj):
    if type_obj == 'UNCHENGED':
        return False
    else:
        return True


def render_plain(ast_tree):
    #print(f'ast_tree {ast_tree}')
    #print(f'ast_test2 {ast_test2}')
    #print(f'ast1 {ast_1}')
    #ast_tree = ast_1
    def iter(ast_tree, path):


        filtered = filter(
            lambda diff_node: filter_AST_for_plain_format(diff_node['type']),
            ast_tree,
        )

       # print(list(filtered))

        output = map(lambda node: select_type_add_return_str(node, path, iter), filtered)

        return '\n'.join(output)

    return iter(ast_tree, path = '')


#print(render_plain(ast_test2))