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
    assert n2.next is None
    print(ll)


def test_add_two():
    n = Node(1)
    ll = Linkedlist()
    print(ll)
    ll.add(n)
    print(ll)
    n2 = Node(2)
    ll.add(n2)
    print(ll)
    n3 = Node(3)
    ll.add(n3)
    assert ll.size == 3
    assert n == ll.head
    assert n.next == n2
    assert n2.next == n3
    assert n3.next is None
    print(ll)


def test_add_nonnode():
    ll = Linkedlist()
    n = 123
    try:
        ll.add(n)
    except Exception as e:
        assert type(e) == TypeError


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


def test_remove():
    ll = Linkedlist()
    n = Node(2)
    ll.add(n)
    print(ll)
    removed_n = ll.remove(2)
    print(ll)
    print(removed_n)
    assert removed_n == n
    assert ll.size == 0
    assert n.next is None


def test_remove_any():
    n = Node(1)
    ll = Linkedlist(n)
    n2 = Node(2)
    ll.add(n2)
    print(ll)
    removed_n = ll.remove_any()
    print(ll)
    print(removed_n)
    assert removed_n == n
    assert ll.size == 1
    assert n2 == ll.head
    assert n.next is None
    assert n2.next is None


def test_iter():
    n1 = Node(1)
    ll = Linkedlist()
    print(ll)
    ll.add(n1)
    print(ll)
    n2 = Node(2)
    ll.add(n2)
    print(ll)
    n3 = Node(3)
    ll.add(n3)
    print(ll)
    for n in ll:
        print(n)
    assert ll.size == 3
    assert n1 == ll.head
    assert n1.next == n2
    assert n2.next == n3
    assert n3.next is None
    print(ll)


def main():
    print('\n test_init_empty:')
    test_init_empty()
    print('\n test_init:')
    test_init()
    print('\n test_empty_add:')
    test_empty_add()
    print('\n test_add:')
    test_add()
    print('\n test_add_two:')
    test_add_two()
    print('\n test_add_nonnode:')
    test_add_nonnode()
    print('\n test_str_empty:')
    test_str_empty()
    print('\n test_repr_empty:')
    test_repr_empty()
    print('\n test_remove:')
    test_remove()
    print('\n test_remove_any:')
    test_remove_any()
    print('\n test_repr:')
    test_repr()
    print('\n test_str:')
    test_str()
    print('\n test_iter:')
    test_iter()


if __name__ == '__main__':
    main()
