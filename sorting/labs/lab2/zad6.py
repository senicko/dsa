"""
Proszę zaproponować strukturę danych, która pozwala wykonywać operacje:
1. Insert
2. RemoveMedian (wyciągnięcie mediany) tak, żeby operacje te działały w czasie O(logn).
"""


class MinHeap:
    def __init__(self):
        self.size = 0
        self.values = []

    # Returns left child of index i.
    left = lambda i: 2 * i + 1

    # Returns right child of index i.
    right = lambda i: 2 * i + 2

    # Returns parent of index i.
    parent = lambda i: (i - 1) // 2

    def heapify(self, i):
        l = MinHeap.left(i)
        r = MinHeap.right(i)
        max_index = i

        if l < self.size and self.values[l] < self.values[max_index]:
            max_index = l

        if r < self.size and self.values[r] < self.values[max_index]:
            max_index = r

        if max_index != i:
            self.values[max_index], self.values[i] = self.values[i], self.values[max_index]
            self.heapify(max_index)

    def insert(self, value):
        if self.size < len(self.values):
            self.values[self.size] = value
        else:
            self.values.append(value)

        self.size += 1
        i = self.size - 1

        while i > 0 and self.values[i] < self.values[MinHeap.parent(i)]:
            self.values[i], self.values[MinHeap.parent(i)] = self.values[MinHeap.parent(i)], self.values[i]
            i = MinHeap.parent(i)

    def pop(self):
        self.size -= 1
        self.values[0], self.values[self.size] = self.values[self.size], self.values[0]
        self.heapify(0)
        return self.values[self.size]

    def top(self):
        return self.values[0]


class Median:
    def __init__(self):
        self.max_heap = MinHeap()
        self.min_heap = MinHeap()

    def insert(self, value):
        # If there are no values in both heaps, insert median
        # to the max heap.
        if self.max_heap.size == 0 and self.min_heap.size == 0:
            self.max_heap.insert(value)
            return

        # Insert value to the correct heap based on top value in max_heap.
        if value <= -self.max_heap.top():
            self.max_heap.insert(-value)
        else:
            self.min_heap.insert(value)

        # Rebalance heaps.
        self._rebalance()


    def remove_median(self):
        median = self.get_median()

        if self.max_heap.size == self.min_heap.size:
            self.min_heap.pop()
            self.max_heap.pop()
        else:
            self.min_heap.pop()
            self._rebalance()

        return median

    def get_median(self):
        return -self.max_heap.top() \
            if self.max_heap.size > self.min_heap.size \
            else (-self.max_heap.top() + self.min_heap.top()) / 2.0

    def _rebalance(self):
        if self.max_heap.size - 1 > self.min_heap.size:
            self.min_heap.insert(-self.max_heap.pop())
        elif self.min_heap.size > self.max_heap.size:
            self.max_heap.insert(-self.min_heap.pop())


if __name__ == "__main__":
    median = Median()

    for x in [1, 2, 2, 2, 3, 3, 6, 7, 7]:
        median.insert(x)

    print("mediana 1:", median.remove_median())
    print("mediana 2:", median.remove_median())
    print("mediana 3:", median.remove_median())
