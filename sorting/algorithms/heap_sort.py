from random import randint

left = lambda i: 2 * i + 1
right = lambda i: 2 * i + 2
parent = lambda i: (i - 1) // 2


def max_heapify(heap, n, i):
    l = left(i)
    r = right(i)
    max_index = i

    if l < n and heap[l] > heap[max_index]:
        max_index = l

    if r < n and heap[r] > heap[max_index]:
        max_index = r

    # If max_index is not i, then we need to "flow" down
    # in the heap with value at index i.
    if max_index != i:
        heap[max_index], heap[i] = heap[i], heap[max_index]
        max_heapify(heap, n, max_index)


def build_max_heap(a):
    n = len(a)

    # Heapify bottom-up starting at index of last inner node.
    for i in range(parent(n - 1), -1, -1):
        max_heapify(a, n, i)


def heap_sort(a):
    n = len(a)
    build_max_heap(a)

    # Top contains maximum element from the array.
    # Shrink the heap. Now n is index of the last leaf.
    # Swap it with the top, so that it's at sorted position in the final array.
    # Run heapify for the leaf, now at index 0, to make sure max heap property is met.

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, i, 0)


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    heap_sort(a)

    # assert
    assert a == expected
    print(a, "ok")
