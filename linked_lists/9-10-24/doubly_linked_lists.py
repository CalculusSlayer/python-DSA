'''
Nayeel Imtiaz
9-10-24

doubly_linked_lists.py
- implementation of doublely linked list
where elements are 2-tuples
'''

from typing import Tuple

class Node:
    def __init__(self, element: Tuple[int, int]):
        self.key, self.value = element
        self.next = None
        self.previous = None

def string_list(list_: Node):
    tokens = []
    while list_:
        tokens.append(f"({list_.key}, {list_.value})")
        list_ = list_.next
    return "[" + ", ".join(tokens) + "]"

def main():
    node1 = Node((1, 1))
    node2 = Node((2, 2))
    node3 = Node((3, 3))

    node1.next = node2
    node2.previous = node1

    node2.next = node3
    node3.previous = node2

    print(f"linked list: {string_list(node1)}")


if __name__ == '__main__':
    main()