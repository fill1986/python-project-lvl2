def create_tree_node(key, first_dict, second_dict):
    first_value = first_dict.get(key)
    second_value = second_dict.get(key)
    if key not in second_dict:
        return {'type': 'DELETED', 'name': key, 'value': first_value}
    if key not in first_dict:
        return {'type': 'ADDED', 'name': key, 'value': second_value}
    if isinstance(first_value, dict) and isinstance(second_value, dict):
        return {
            'type': 'NESTED',
            'name': key,
            'children': create_diff_tree(first_value, second_value)
        }
    if first_value == second_value:
        return {'type': 'UNCHANGED', 'name': key, 'value': first_value}

    return {
        'type': 'CHANGED',
        'name': key,
        'value_before': first_value,
        'value_after': second_value,
    }


def create_diff_tree(first_data, second_data):
    uniq_keys = sorted(first_data.keys() | second_data.keys())

    ast = map(
        lambda key: create_tree_node(key, first_data, second_data), uniq_keys
    )
    return list(ast)
