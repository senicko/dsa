"""
Proszę zaimplementować operację wstawiania elementu do kopca binarnego.
"""


left = lambda i: 2 * i + 1
right = lambda i: 2 * i + 2
parent = lambda i: (i - 2) // 2


def heapify(heap, n, i):
    l = left(i)
    r = right(i)
    max_index = i

    if l < n and heap[l] > heap[max_index]:
        max_index = l

    if r < n and heap[r] > heap[max_index]:
        max_index = r

    if max_index != i:
        heap[max_index], heap[i] = heap[i], heap[max_index]
        heapify(heap, n, max_index)


def build_heap(a):
    n = len(a)

    for i in range(parent(n - 1), 0, -1):
        heapify(a, n, i)


def insert_heap(heap, n, value):
    # We assume that our heap is dynamically sized.
    if n < len(heap):
        heap[n] = value
    else:
        heap.append(value)

    n += 1
    i = n - 1

    while i > 0 and heap[parent(i)] < value:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)

    # Return new heap length back to the caller
    return n


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    build_heap(a)
    print(a)

    insert_heap(a, len(a) - 1, 10)
    print(a)
