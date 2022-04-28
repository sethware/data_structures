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
        if isinstance(other, Node):
            return self.value == other.value and self.next == other.next and self.left == other.left and self.right == other.right
        elif self or other is None:
            if self is other:
                return True
        else:
            return False

    def __repr__(self):
        return str({'value': self.value, 'next': str(self.next), 'left': str(self.left), 'right': str(self.right)})

    # def __str__(self):
    #     return str(self.__repr__)
