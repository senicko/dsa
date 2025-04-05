left = lambda i: 2 * i + 1
right = lambda i: 2 * i + 2
parent = lambda i: (i - 1) // 2


def heapify(a, n, i):
    l = left(i)
    r = right(i)
    max_index = i

    if l < n and a[l] > a[max_index]:
        max_index = l

    if r < n and a[r] > a[max_index]:
        max_index = r

    if max_index != i:
        a[max_index], a[i] = a[i], a[max_index]
        heapify(a, n, max_index)


def buildheap(a):
    n = len(a)

    for i in range(parent(n - 1), -1, -1):
        heapify(a, n, i)


def heapsort(a):
    n = len(a)
    buildheap(a)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


def binary_search(a, x):
    n = len(a)
    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if a[mid] == x:
            return True
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return False


def find_pairs(a, b, x):
    # Sorting takes O(nlogn)
    heapsort(a)
    heapsort(b)

    # Linear scan with binary search, O(nlogn)
    for v in a:
        if binary_search(b, x - v):
            return (v, x - v)

    return None


if __name__ == "__main__":
    print(find_pairs([1, 2, 3, 4], [1, 3, 4, 6], 10))
