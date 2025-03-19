MAX_HEAP = "max_heap"
MIN_HEAP = "min_heap"


# Node is a class that tracks value's heap and index.
# It allows us to find in which heap value resides and
# at what index it is in O(1) time.
class Node:
    def __init__(self, value, index=None, heap=None):
        self.value = value
        self.index = index
        self.heap = heap

    def __neg__(self):
        self.value *= -1
        return self

    def swap_index(self, other):
        self.index, other.index = other.index, self.index


# MinHeap implementation that manages Nodes and updates their
# indexes during heap operations.
class MinHeap:
    def __init__(self, n, id=None):
        self.heap = [None] * n
        self.size = 0
        self.id = id

    left = lambda i: 2 * i + 1
    right = lambda i: 2 * i + 2
    parent = lambda i: (i - 1) // 2

    def top(self):
        return self.heap[0].value

    def heapify_down(self, i):
        l = MinHeap.left(i)
        r = MinHeap.right(i)
        min_index = i

        if l < self.size and self.heap[l].value < self.heap[min_index].value:
            min_index = l

        if r < self.size and self.heap[r].value < self.heap[min_index].value:
            min_index = r

        if min_index != i:
            self.heap[min_index].swap_index(self.heap[i])
            self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]
            self.heapify_down(min_index)

    def heapify_up(self, i):
        p = MinHeap.parent(i)

        if i > 0 and self.heap[p].value > self.heap[i].value:
            self.heap[p].swap_index(self.heap[i])
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            self.heapify_up(p)

    def insert(self, value):
        value.heap = self.id
        value.index = self.size
        self.heap[self.size] = value

        # Make sure min heap property is maintained
        self.heapify_up(self.size)

        self.size += 1

    def remove(self, i):
        self.size -= 1

        removed = self.heap[i]
        self.heap[self.size].swap_index(self.heap[i])
        self.heap[self.size], self.heap[i] = self.heap[i], self.heap[self.size]

        if self.size != i:
            # Make sure min heap property is maintained
            self.heapify_up(i)
            self.heapify_down(i)

        return removed


def ksum(T, k, p):
    n = len(T)

    for i in range(n):
        T[i] = Node(T[i])

    min_heap = MinHeap(n, MIN_HEAP)
    max_heap = MinHeap(n, MAX_HEAP)

    # Load first k values to min_heap.
    for i in range(k):
        min_heap.insert(T[i])

    # Load the rest of p first values to min_heap or max_heap
    # maintaining the property that min_heap keeps the k largest
    # values in the window.
    for i in range(k, p):
        if T[i].value > min_heap.top():
            max_heap.insert(-min_heap.remove(0))
            min_heap.insert(T[i])
        else:
            max_heap.insert(-T[i])

    total = 0

    for i in range(p, n):
        # Add the kth largest element from previous window to total sum.
        total += min_heap.top()

        # Get outgoing and incoming nodes.
        outgoing = T[i - p]
        incoming = T[i]

        # Remove outgoing node from its heap.
        # Insert incoming node to appropriate heap.

        min_heap.remove(outgoing.index) if outgoing.heap == MIN_HEAP else max_heap.remove(outgoing.index)
        min_heap.insert(incoming)

        # It's possible that after removing outgoing node
        # max_heap's top belongs to the kth largest ones.

        if max_heap.size > 0:
            min_heap.insert(-max_heap.remove(0))

        # Balance min_heap so that it contains exactly k values.
        while min_heap.size > k:
            max_heap.insert(-min_heap.remove(0))

    return total + min_heap.top()
