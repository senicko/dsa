from typing import Self, cast


class Node:
    def __init__(self, value=None, next=None):
        self.value = value 
        self.next = next

    @staticmethod
    def from_list(values):
        dummy = Node()
        head = dummy

        for v in values:
            new = Node(v)
            head.next = new
            head = new

        return dummy


def print_list(p):
    curr = p.next
    while curr:
        print(curr.value, end=" -> ")
        curr = curr.next
    print("None")


# Extracts parent of a node with minimum value.
def extract_min(p):
    min_p = p
    prev = p.next
    curr = prev.next

    while curr:
        if curr.value < min_p.next.value:
            min_p = prev

        prev = curr
        curr = curr.next

    return min_p


# Inserts a node at sorted position to the list with sentinel.
def insert_sorted(p, new):
    prev = p
    curr = p.next

    while curr:
        if curr.value > new.value:
            prev.next = new
            new.next = curr
            break

        prev = curr
        curr = curr.next

    if curr is None:
        prev.next = new


def selection_sort(p):
    # Head points to the last element in the sorted prefix.
    head = p.next

    while head and head.next:
        if head.value > head.next.value:
            # Find parent of the minimum node 
            # in the remaining list
            min_p = extract_min(head)
            min_node = min_p.next

            # Detach minimum node
            min_p.next = min_p.next.next
            min_node.next = None

            # Insert min node into sorted list
            insert_sorted(p, min_node)
        else:
            head = head.next


for test in [
    [3, 6, 2, 4, 6, 2, 5, 2, 5],
    [],
    [1],
    [7, 6, 5, 4, 3]
]:
    ll = Node.from_list(test)
    selection_sort(ll)
    print_list(ll)
