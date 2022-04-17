from node import Node
from tree import Tree


def test_init():
    n = Node(1)
    t = Tree(n)
    print(n)
    print(t)
    assert n is not None
    assert t is not None
    assert t.size == 1
    assert t.head == n


def test_init_empty():
    t = Tree()
    print(t)
    assert t is not None
    assert t.head is None
    assert t.size == 0


def main():
    print('\n test_init:')
    test_init()


if __name__ == '__main__':
    main()
