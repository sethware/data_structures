from my_queue import MyQueue
from node import Node


def test_init_empty():
    q = MyQueue()
    assert q.size == 0
    print(q)


def test_init():
    n = Node(1)
    q = MyQueue(n)
    assert q.size == 1
    assert n == q.head
    print(q)


def test_empty_add():
    n = Node(1)
    q = MyQueue()
    print(q)
    q.add(n)
    assert q.size == 1
    assert n == q.head
    print(q)


def test_add():
    n = Node(1)
    q = MyQueue(n)
    print(q)
    n2 = Node(2)
    q.add(n2)
    assert q.size == 2
    assert n == q.head
    assert n.next == n2
    assert n2.next is None
    print(q)


def test_add_two():
    n = Node(1)
    q = MyQueue()
    print(q)
    q.add(n)
    print(q)
    n2 = Node(2)
    q.add(n2)
    print(q)
    n3 = Node(3)
    q.add(n3)
    assert q.size == 3
    assert n == q.head
    assert n.next == n2
    assert n2.next == n3
    assert n3.next is None
    print(q)


def test_add_nonnode():
    q = MyQueue()
    n = 123
    try:
        q.add(n)
    except Exception as e:
        assert type(e) == TypeError


def test_str_empty():
    q = MyQueue()
    print(q)


def test_repr_empty():
    q = MyQueue()
    print(q.__repr__())


def test_str():
    q = MyQueue()
    n = Node(1)
    q.add(n)
    print(q)


def test_repr():
    q = MyQueue()
    n = Node(1)
    q.add(n)
    print(q.__repr__())


def test_remove():
    n = Node(1)
    q = MyQueue(n)
    n2 = Node(2)
    print(q)
    removed_n = q.remove()
    print(q)
    print(removed_n)
    assert removed_n == n
    assert q.size == 0
    q.add(n2)
    print(q)
    assert q.size == 1
    assert q.head is n2
    removed_n = q.remove()
    print(q)
    print(removed_n)
    assert removed_n == n2
    assert q.size == 0
    assert q.head is None
    assert n.next is None
    assert n2.next is None


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
    print('\n test_repr:')
    test_repr()
    print('\n test_str:')
    test_str()


if __name__ == '__main__':
    main()
