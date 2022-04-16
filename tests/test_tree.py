import node.node as node
import tree.tree as tree


def test_init():
    n = node.Node()
    t = tree.Tree(n)
    print('in test')
    assert n is not None
    assert t is not None
