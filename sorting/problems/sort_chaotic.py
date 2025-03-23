class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    @staticmethod
    def from_list(values):
        dummy = Node()
        head = dummy

        for v in values:
            new = Node(v)
            head.next = new
            head = new

        return dummy.next

    def print(self):
        curr = self

        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

        print("*")


left = lambda i: 2 * i + 1
right = lambda i: 2 * i + 2
parent = lambda i: (i - 1) // 2


def heapify(heap, n, i):
    l = left(i)
    r = right(i)
    min_index = i

    if l < n and heap[l].val < heap[min_index].val:
        min_index = l

    if r < n and heap[r].val < heap[min_index].val:
        min_index = r

    if min_index != i:
        heap[min_index], heap[i] = heap[i], heap[min_index]
        heapify(heap, n, min_index)


def insert_heap(heap, n, node):
    heap[n] = node
    n += 1
    i = n - 1

    while i > 0 and heap[i].val < heap[parent(i)].val:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

    return n


def pop_heap(heap, n):
    top = heap[0]
    n -= 1
    heap[0], heap[n] = heap[n], heap[0]
    heapify(heap, n, 0)
    return top, n


def sort_chaotic(p, k):
    dummy = Node()
    head = dummy

    heap = [None] * (k + 1)
    heap_size = 0

    def append():
        nonlocal heap_size, head
        top, heap_size = pop_heap(heap, heap_size)
        top.next = None
        head.next = top
        head = head.next

    curr = p

    while curr:
        tmp = curr.next

        # Fill heap with k + 1 values
        if heap_size < k + 1:
            heap_size = insert_heap(heap, heap_size, curr)

        # If we have k values on the heap remove the
        # smallest one as it can't be anywhere else.
        if heap_size == k + 1:
            append()

        curr = tmp

    while heap_size > 0:
        append()

    return dummy.next


if __name__ == "__main__":
    p = Node.from_list([1, 0, 3, 2, 4, 6, 5])
    k = 1

    sorted = sort_chaotic(p, k)
    sorted.print()
