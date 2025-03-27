"""
Proszę zaimplementować operację która mając na wejściu dwie posortowane listy jednokierunkowe-
kowe zwraca posortowaną listę zawierającą wszystkie elementy list wejściowych.
"""


class Node:
    def __init__(self):
        self.value = None
        self.next = None

    def __repr__(self):
        out = "["
        curr = self
        while curr:
            out += f"{curr.value}->"
            curr = curr.next
        out += "]"
        return out

    @staticmethod
    def from_list(values: list[int]):
        dummy = Node()
        head = dummy

        for v in values:
            new = Node()
            new.value = v
            head.next = new
            head = new

        return dummy.next


def merge_lists(p: Node, q: Node):
    dummy = Node()
    prev = dummy

    # While both p and q are some nodes.
    while p and q:
        # Pick node with the smallest value.
        if p.value < q.value:
            prev.next = p  # Chain it with prev
            prev = p  # Set prev to p
            p = p.next  # Advance p
        else:
            prev.next = q
            prev = q
            q = q.next

    # At this point we have finished visiting nodes in p or q.
    # We have to attach the rest of the list which wasn't fully visited.

    if p:
        prev.next = p

    if q:
        prev.next = q

    return dummy.next


if __name__ == "__main__":
    a = Node.from_list([1, 3, 5, 7, 9, 11])
    b = Node.from_list([2, 4, 6, 8, 10, 12, 14, 16])
    out = merge_lists(a, b)
    print(out)
