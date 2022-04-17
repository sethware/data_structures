from linkedlist import Linkedlist
from node import Node


def test_init_empty():
    ll = Linkedlist()
    assert ll.size == 0


def test_init():
    n = Node()
    ll = Linkedlist(n)
    assert ll.size == 1
    assert n == ll.head
    print(ll)


def test_empty_add():
    n = Node()
    ll = Linkedlist()
    ll.add(n)
    assert ll.size == 1
    assert n == ll.head
    print(ll)


def test_add():
    n = Node()
    ll = Linkedlist(n)
    n2 = Node()
    ll.add(n2)
    assert ll.size == 2
    assert n == ll.head
    assert n.next == n2
    print(ll)
