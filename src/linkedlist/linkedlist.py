from dataclasses import dataclass
from node import node


@dataclass
class Linkedlist():
    head: node.Node
    size: int

    def __init__(self, head: node.Node = None):
        self.size = 0
        self.head = head
        if head is not None and isinstance(head, node.Node):
            self.size += 1

    def add(self, n: node.Node):
        prev = self.head
        if prev is None and isinstance(n, node.Node):
            self.head = n
            self.size += 1
            return
        elif isinstance(n, node.Node):
            next = prev.next
            while next is not None:
                prev = next
                next = prev.next
            prev.next = n
            node.next = None
