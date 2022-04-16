from node import node


def test_init():
    n = node.Node()
    print('in test')
    assert n is not None
