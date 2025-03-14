from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def bucket_sort(a, limit):
    n = len(a)

    # Create bucket for each value
    buckets = [[b := Node(), b] for _ in range(limit + 1)]

    # Iterate through values inarray a and insert
    # them in correct buckets.
    for i in range(n):
        new = Node(a[i])
        idx = a[i]
        buckets[idx][1].next = new
        buckets[idx][1] = new

    # Iterate through buckets (which are stored in sorted order)
    # and dump values back to a.
    i = 0

    for bucket in buckets:
        curr = bucket[0].next

        while curr:
            a[i] = curr.value
            curr = curr.next
            i += 1


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    bucket_sort(a, max(a))

    # assert
    assert a == expected
    print(a, "ok")
