from dataclasses import dataclass
from node import Node


@dataclass
class Linkedlist():
    head: Node
    size: int

    def __init__(self, head: Node = None):
        self.size = 0
        self.head = head
        if head is not None and isinstance(head, Node):
            self.size += 1

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
        else:
            raise TypeError("Can't add non-Node type to Linkedlist")
