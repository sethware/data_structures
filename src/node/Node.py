from dataclasses import dataclass

@dataclass
class Node:
    def __init__(self):
        self.value = None
        self.next = None

    # def __repr__(self):
    #     return str(self.value,self.next)

    # def __str__(self):
    #     return str(self.__repr__)
