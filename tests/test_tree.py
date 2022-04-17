from node import Node
from tree import Tree


def test_init():
    n = Node()
    t = Tree(n)
    print('in test')
    assert n is not None
    assert t is not None
