from node import Node


def test_init_empty():
    n = Node()
    assert n is not None
    assert n.value is None
    assert n.next is None
    assert n.left is None
    assert n.right is None


def test_init():
    n = Node(1)
    assert n is not None
    assert n.value == 1
    assert n.next is None
    assert n.left is None
    assert n.right is None


def test_connect():
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
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
    assert n1.next is None
    assert n2.next is None
    assert n1.left is None
    assert n2.left is None
    assert n1.right is None
    assert n2.right is None
