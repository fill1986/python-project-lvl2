
def transform_value_to_str(node_value):
    if isinstance(node_value, bool):
        return str(node_value).lower()
    if node_value is None:
        return 'null'

    return str(node_value)


def stringify(node_data):
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
        return function(node['children'], f"{parent}{node['name']}.")


def filter_AST_for_plain_format(type_obj):
    if type_obj == 'UNCHANGED':
        return False
    else:
        return True


def render_plain(ast_tree):
    def iter(ast_tree, path):

        filtered = filter(
            lambda diff_node: filter_AST_for_plain_format(diff_node['type']),
            ast_tree,
        )

        output = map(lambda node: select_type_add_return_str(
            node, path, iter), filtered)

        return '\n'.join(output)

    return iter(ast_tree, path='')
