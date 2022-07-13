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
            function(node['children'], depth + 2),
        )

    elif type == 'ADDED':

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

    def iter_(current_value, depth=0):

        result = map(lambda s_type: select_type(s_type, depth, s_type['type'], iter_), current_value)

        return '{{\n{0}\n{1}}}'.format(
            '\n'.join(result),
            set_indent(depth - 1),
        )

    return iter_(value, 1)
