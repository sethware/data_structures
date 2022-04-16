from linkedlist import Linkedlist
from node import Node


def test_init_empty():
    ll = Linkedlist()
    print(ll)


def test_init():
    n = Node()
    ll = Linkedlist(n)
    print(ll)


def test_empty_add():
    n = Node()
    ll = Linkedlist()
    ll.add(n)
    print(ll)


def test_add():
    n = Node()
    ll = Linkedlist(n)
    n2 = Node()
    ll.add(n2)
    print(ll)
