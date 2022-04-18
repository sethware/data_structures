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


def test_add():
    t = Tree()
    n1 = Node(1)
    n2 = Node(2)
    print(t)
    t.add(n1)
    print(t)
    assert t.size == 1
    t.add(n2)
    print(t)
    assert t.size == 2


def test_remove_any():
    t = Tree()
    n1 = Node(1)
    n2 = Node(2)
    t.add(n1)
    print(t)
    removed_n = t.remove_any()
    print(t)
    assert removed_n is n1
    assert t.size == 0
    t.add(n2)
    t.add(n1)
    print(t)
    removed_n = t.remove_any()
    print(t)
    assert t.size == 1
    assert isinstance(removed_n, Node)


def test_remove_any_empty():
    t = Tree()
    print(t)
    removed_n = t.remove_any()
    assert removed_n is None


def main():
    print('\n test_init')
    test_init()
    print('\n test_init_empty')
    test_init_empty()
    print('\n test_add')
    test_add()
    print('\n test_remove_any')
    test_remove_any()
    print('\n test_remove_any_empty')
    test_remove_any_empty()


if __name__ == '__main__':
    main()
