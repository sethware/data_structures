from dataclasses import dataclass
from node import Node


@dataclass
class MyQueue():
    head: Node
    size: int

    def __init__(self, head: Node = None):
        self.size = 0
        self.head = head
        if head is not None and isinstance(head, Node):
            self.size += 1

    def __str__(self):
        ret_str = ""
        curr = self.head
        while curr is not None:
            ret_str = ret_str + str(curr) + '->'
            curr = curr.next
        return '{' + ret_str + '[None]}'

    def __repr__(self):
        ret_str = ""
        curr = self.head
        while curr is not None:
            ret_str = ret_str + curr.__repr__() + ',\n'
            curr = curr.next
        return '{' + ret_str + '{None}}'

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
        curr = self.head
        next = curr.next
        if curr is None:
            return None
        while curr is not None:
            if next is None:
                if curr is self.head:
                    self.head = None
                curr.next = None
                self.size -= 1
                return curr
            curr = next
            next = curr.next
