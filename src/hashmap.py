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
        # print(f'\n hash code: {hash_code}\n')
        # print(f'self.array[hash_code]: {self.array[hash_code]}\n')

        for n in self.array[hash_code]:
            # print(f'checking node: {n} for key: {key}\n')
            # print(f'node.value[key]: {type(n.value["key"])}\n')
            # print(f'key: {type(key)}\n')
            # print(f'node.value[key] == key:{int(n.value["key"]) == key}\n')
            if int(n.value['key']) == key:
                return n.value['value']
        return None

    def remove(self, value=None, key: str = None):
        if key is None or value is None:
            raise KeyError('Must provide either a value or a key/hash to Hashmap.remove()')

        hash_code = self.hash(value) % len(self.array)

        for n in self.array[hash_code]:
            if int(n.value['key']) == key:
                print(f'self.array[hash_code]: {self.array[hash_code]}\n')
                print(f'n: {n}\n')
                print(f'n in array?: {n in self.array[hash_code]}')
                n = self.array[hash_code].remove(n.value)
                print(f'n: {n}\n')
                if n is not None:
                    self.size -= 1
                    return n.value['value']
        return None
