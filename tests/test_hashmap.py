import pytest
from hashmap import Hashmap


def test_init():
    h = Hashmap()
    print(h)
    assert h is not None
    assert h.size == 0


def test_add():
    h = Hashmap()
    print(h)
    val = 15
    key = '15'
    h.add(key, val)
    assert h.size == 1


@pytest.mark.xfail
def test_find():
    h = Hashmap()
    val = 15
    key = '15'
    h.add(key, val)
    print(h)
    n = h.find(key, val)
    print(f'hashmap:\n {h}')
    print(f'found value:\n {n}')
    assert h.size == 1
    assert n == val
    assert n is val


@pytest.mark.xfail
def test_remove():
    h = Hashmap()
    val = 15
    key = '15'
    h.add(key, val)
    print(f'{h}\n')
    n = h.remove(key, val)
    print(f'hashmap:\n {h}')
    print(f'removed value:\n {n}')
    assert h.size == 0
    assert n == val
    assert n is val
