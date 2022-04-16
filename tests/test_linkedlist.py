from linkedlist import linkedlist
from node import node


def test_init_empty():
    ll = linkedlist.Linkedlist()
    print(ll)


def test_init():
    n = node.Node()
    ll = linkedlist.Linkedlist(n)
    print(ll)


def test_empty_add():
    n = node.Node()
    ll = linkedlist.Linkedlist()
    ll.add(n)
    print(ll)


def test_add():
    n = node.Node()
    ll = linkedlist.Linkedlist(n)
    n2 = node.Node()
    ll.add(n2)
    print(ll)
