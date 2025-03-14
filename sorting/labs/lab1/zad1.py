from typing import Self, cast


class Node:
    def __init__(self):
        self.value: int = cast(int, None)
        self.next: Self | None = None
        self.prev: Self | None = None

    @staticmethod
    def from_list(values: list[int]):
        dummy = Node()
        head = dummy

        for v in values:
            new = Node()
            new.value = v
            head.next = new
            head = new

        return dummy


def find_max(p: Node):
    max_value = -1
    curr_node = p.next

    while curr_node:
        if curr_node.value > max_value:
            max_value = curr_node.value
        curr_node = curr_node.next

    return max_value


ll = Node.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(find_max(ll))
