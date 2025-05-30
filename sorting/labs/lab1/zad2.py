from typing import Self, cast


class Node:
    def __init__(self):
        self.value: int = cast(int, None)
        self.next: Self | None = None

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

    def __repr__(self):
        out = "["
        curr = self.next
        while curr:
            out += f"{curr.value}->"
            curr = curr.next
        out += "]"
        return out


def insert_sorted(p: Node, v: int):
    prev = p
    curr = p.next

    new = Node()
    new.value = v

    while curr:
        if curr.value > v:
            prev.next = new
            new.next = curr
            break

        prev = curr
        curr = curr.next

    if curr is None:
        prev.next = new


ll = Node.from_list([1, 2, 3, 4, 5, 7, 8, 9])
insert_sorted(ll, 6)
print(ll)
