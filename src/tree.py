import node.node as Node
from dataclasses import dataclass


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

    def add(self, n: Node)


def main():
    node = Node.Node()
    tree = Tree(node)
    print(f'tree: {tree}')


if __name__ == '__main__':
    main()
