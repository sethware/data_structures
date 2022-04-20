from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, value=None, next=None, left=None, right=None):
        self.value = value
        self.next = next
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.value}]'

    def __eq__(self, other):
        return self is other

    def __repr__(self):
        return str({'value': self.value, 'next': str(self.next), 'left': str(self.left), 'right': str(self.right)})

    # def __str__(self):
    #     return str(self.__repr__)
