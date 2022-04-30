from dataclasses import dataclass
from node import Node
from linkedlist import Linkedlist

@dataclass
class MyQueue(Linkedlist):
    head: Node
    size: int

    def __init__(self, n: Node=None):
        if n is None:
            return super().__init__()
        return super().__init__(n)

    def add(self, n: Node):
        prev = self.head
        if prev is None and isinstance(n, Node):
            self.head = n
            self.size += 1
            return
        elif isinstance(n, Node):
            prev = self.head
            next = prev.next
            while next is not None:
                prev = next
                next = prev.next
            prev.next = n
            n.next = None
            self.size += 1
        else:
            raise TypeError("Can't add non-Node type to Linkedlist")

    def remove(self):
        return super().remove_any()
