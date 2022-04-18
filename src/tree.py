from dataclasses import dataclass
from node import Node


@dataclass
class Tree:
    head: Node
    size: int

    def __init__(self, head: Node = None):
        self.head = head
        if head is not None:
            self.size = 1
        else:
            self.size = 0

    def add(self, n: Node):
        n.left = None
        n.right = None
        n.next = None
        if self.head is None:
            self.head = n
            self.size += 1
        else:
            checked_ns = set()
            curr = self.head
            while curr is not None:
                if curr.left is None:
                    curr.left = n
                    self.size += 1
                    return
                elif curr.right is None:
                    curr.right = n
                    self.size += 1
                    return
                checked_ns.add(curr)
                curr = curr.left

    def remove_any(self):
        prev = None
        curr = self.head
        if curr is None:
            return None
        while curr is not None:
            if curr.left is None and curr.right is None:
                if prev is not None:
                    prev.next = None
                self.size -= 1
                if curr is self.head:
                    self.head = None
                return curr
            prev = curr
            if prev.left is None:
                curr = prev.right
            else:
                curr = prev.left


def main():
    node = Node()
    tree = Tree(node)
    print(f'tree: {tree}')


if __name__ == '__main__':
    main()
