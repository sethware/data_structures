import node.Node as Node
import tree.Tree as Tree


def test_init():
    n = Node.Node()
    t = Tree.Tree(n)
    print('in test')
    assert n is not None
    assert t is not None
