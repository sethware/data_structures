from linkedlist import Linkedlist
from node import Node


def test_init_empty():
    ll = Linkedlist()
    assert ll.size == 0
    print(ll)


def test_init():
    n = Node(1)
    ll = Linkedlist(n)
    assert ll.size == 1
    assert n == ll.head
    print(ll)


def test_empty_add():
    n = Node(1)
    ll = Linkedlist()
    print(ll)
    ll.add(n)
    assert ll.size == 1
    assert n == ll.head
    print(ll)


def test_add():
    n = Node(1)
    ll = Linkedlist(n)
    print(ll)
    n2 = Node(2)
    ll.add(n2)
    assert ll.size == 2
    assert n == ll.head
    assert n.next == n2
    print(ll)


def test_str_empty():
    ll = Linkedlist()
    print(ll)


def test_repr_empty():
    ll = Linkedlist()
    print(ll.__repr__())


def test_str():
    ll = Linkedlist()
    n = Node(1)
    ll.add(n)
    print(ll)


def test_repr():
    ll = Linkedlist()
    n = Node(1)
    ll.add(n)
    print(ll.__repr__())


def main():
    print('\n test_init_empty:')
    test_init_empty()
    print('\n test_init:')
    test_init()
    print('\n test_empty_add:')
    test_empty_add()
    print('\n test_add:')
    test_add()
    print('\n test_str_empty:')
    test_str_empty()
    print('\n test_repr_empty:')
    test_repr_empty()
    print('\n test_repr:')
    test_repr()
    print('\n test_str:')
    test_str()


if __name__ == '__main__':
    main()
