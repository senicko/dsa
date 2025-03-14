"""
Proszę zaimplementować MergeSort dla listy jednokierunkowej.
"""

from zad2 import merge_lists

class Node:
    def __init__(self):
        self.value = None
        self.next = None

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


    def print(self):
        curr = self
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")


def extract_mid(l, n):
    # We want to use this function only
    # when there are at least 2 nodes.
    assert n > 1

    # Find middle node index and subtract one
    # to select middle node's parent.
    mid = (n // 2) - 1

    while mid > 0:
        l = l.next
        mid -= 1

    # Keep pointer to middle node
    # and detach halves from each other.
    mid = l.next
    l.next = None

    return mid


def merge_sort(l):
    # Find number of nodes in list a.
    n = 0
    curr = l
    while curr:
        n += 1
        curr = curr.next

    # The actual merge sort algorithm.
    def sort(l, n):
        if not l.next:
            return l

        # If our list has at least two elements.
        if l.next:
            mid = extract_mid(l, n)
            l = sort(l, n // 2)
            mid = sort(mid, n - (n // 2))
            return merge_lists(l, mid)

    return sort(l, n)


if __name__ == "__main__":
    l = Node.from_list([13, 5, 31, 4, 212, 5, 6])
    merge_sort(l).print()
