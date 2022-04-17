from node import Node


def test_init_empty():
    n = Node()
    print(n)
    print(n.__repr__())
    assert n is not None
    assert n.value is None
    assert n.next is None
    assert n.left is None
    assert n.right is None


def test_init():
    n = Node(1)
    print(n)
    print(n.__repr__())
    assert n is not None
    assert n.value == 1
    assert n.next is None
    assert n.left is None
    assert n.right is None


def test_connect():
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    print(n1)
    print(n1.__repr__())
    print(n2)
    print(n2.__repr__())
    assert n1.next == n2
    assert n2.next is None
    assert n1.left is None
    assert n2.left is None
    assert n1.right is None
    assert n2.right is None


def test_disconnect():
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n1.next = None
    print(n1)
    print(n1.__repr__())
    print(n2)
    print(n2.__repr__())
    assert n1.next is None
    assert n2.next is None
    assert n1.left is None
    assert n2.left is None
    assert n1.right is None
    assert n2.right is None


def main():
    print('\n test_init_empty:')
    test_init_empty()
    print('\n test_init:')
    test_init()
    print('\n test_connect:')
    test_connect()
    print('\n test_disconnect:')
    test_disconnect()


if __name__ == '__main__':
    main()
