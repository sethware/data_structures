from dataclasses import dataclass
from node import Node


@dataclass
class Linkedlist():
    head: Node
    size: int

    def __init__(self, head: Node = None):
        self.size = 0
        if head is not None and isinstance(head, Node):
            self.head = head
            self.size += 1

    def add(self, node: Node):
        prev = self.head
        next = prev.next
        while next is not None:
            prev = next
            next = prev.next
        prev.next = node
        node.next = None
