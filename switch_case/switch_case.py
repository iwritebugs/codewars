def eval_object(v):
    operations = {
        "+": v['a'] + v['b'],
        "-": v['a'] - v['b'],
        "/": v['a'] / v['b'],
        "*": v['a'] * v['b'],
        "%": v['a'] % v['b'],
        "**": v['a'] ** v['b']
    }

    return operations.get(v['operation'], 1)


def test_eval_object():
    assert eval_object({'a': 1, 'b': 1, 'operation': '+'}) == 2
    assert eval_object({'a': 1, 'b': 1, 'operation': '-'}) == 0
    assert eval_object({'a': 1, 'b': 1, 'operation': '/'}) == 1
    assert eval_object({'a': 1, 'b': 1, 'operation': '*'}) == 1
    assert eval_object({'a': 1, 'b': 1, 'operation': '%'}) == 0
    assert eval_object({'a': 1, 'b': 1, 'operation': '**'}) == 1
