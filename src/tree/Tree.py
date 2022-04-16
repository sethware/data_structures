import node.node as Node
from dataclasses import dataclass

@dataclass
class Tree:
    head: Node
    size: int
    def __init__(self,head:Node):
        self.head = head
        self.size = 0

def main():
    node = Node.Node()
    tree = Tree(node)
    print(f'tree: {tree}')

if __name__ == '__main__':
    main()
