import hashlib
from dataclasses import dataclass
from linkedlist import Linkedlist
from node import Node


@dataclass
class Hashmap():
    array: list[Linkedlist]
    size: int

    def add(self, key: str, value):
        val_dict = {'key': key, 'value': value}
        hash_code = self.hash(key) % len(self.array)
        value_node = Node(val_dict)
        self.array[hash_code].add(value_node)
        self.size += 1

    def __init__(self, value=None):
        self.array = [Linkedlist()]
        self.size = 0
        if value is not None:
            self.add(value)

    def hash(self, value: str):
        return int(hashlib.md5(value.encode('utf-8')).hexdigest(), 16)

    def find(self, value=None, key: str = None):
        if key is None or value is None:
            raise KeyError('Must provide either a value or a key/hash to Hashmap.find()')

        hash_code = self.hash(value) % len(self.array)

        for n in self.array[hash_code]:
            if n.value['key'] == key:
                return n.value['value']
        return None

    def remove(self, value=None, key: str = None):
        if key is None or value is None:
            raise KeyError('Must provide either a value or a key/hash to Hashmap.remove()')

        hash_code = self.hash(value) % len(self.array)

        for n in self.array[hash_code]:
            if n.value['key'] == key:
                n = self.array[hash_code].remove(n)
                if n is not None:
                    self.size -= 1
                    return n.value['value']
        return None
