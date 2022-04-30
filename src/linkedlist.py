from dataclasses import dataclass
from node import Node


@dataclass
class Linkedlist():
    '''An iterable custom linked list implementation'''
    head: Node
    size: int

    def __init__(self, head: Node = None):
        self.size = 0
        self.head = head
        if head is not None and isinstance(head, Node):
            self.size += 1

    def __len__(self):
        return self.size

    def __iter__(self):
        self.current = Node(next=self.head)
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            self.current = self.current.next
            if self.current is None:
                raise StopIteration
        return self.current

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

    def remove(self, value):
        prev = None
        curr = self.head
        next = curr.next
        if curr is None:
            return None
        while curr is not None:
            if curr.value == value:
                if self.head is curr:
                    self.head = next
                elif prev is not None:
                    prev.next = next
                curr.next = None
                self.size -= 1
                return curr
            prev = curr
            curr = next
            if curr is not None:
                next = curr.next
            else:
                next = None
        return None

        def remove_node(self, n):
            prev = None
            curr = self.head
            next = curr.next
            if curr is None:
                return None
            while curr is not None:
                if curr == value:
                    if self.head is curr:
                        self.head = next
                    elif prev is not None:
                        prev.next = next
                    curr.next = None
                    self.size -= 1
                    return curr
                prev = curr
                curr = next
                if curr is not None:
                    next = curr.next
                else:
                    next = None
            return None

    def remove_any(self):
        curr = self.head
        if curr is None:
            return None
        elif curr.next is not None:
            self.head = curr.next
            curr.next = None
            self.size -= 1
            return curr
        else:
            self.head = curr.next
            curr.next = None
            self.size -= 1
            return curr
        return None
