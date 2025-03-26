LEFT = 0
RIGHT = 1
COUNT = 2

left = lambda i: 2 * i + 1
right = lambda i: 2 * i + 2
parent = lambda i: (i - 1) // 2


def merge(L, l, mid, r):
    left = L[l:mid + 1]
    right = L[mid + 1: r + 1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i][LEFT] > right[j][LEFT] or \
                (left[i][LEFT] == right[j][LEFT] and left[i][RIGHT] < right[j][RIGHT]):
            L[k] = left[i]
            i += 1
        else:
            L[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        L[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        L[k] = right[j]
        j += 1
        k += 1


def mergesort(L, l, r):
    if l < r:
        mid = l + (r - l) // 2
        mergesort(L, l, mid)
        mergesort(L, mid + 1, r)
        merge(L, l, mid, r)


def max_rank_merge(L, l, mid, r):
    left = L[l:mid + 1]
    right = L[mid + 1: r + 1]

    i = 0
    j = 0
    k = l

    counter = 0

    while i < len(left) and j < len(right):
        if left[i][RIGHT] <= right[j][RIGHT]:
            L[k] = left[i]
            counter += 1
            i += 1
        else:
            L[k] = right[j]
            right[j][COUNT] += counter
            j += 1
        k += 1

    while i < len(left):
        L[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        L[k] = right[j]
        right[j][COUNT] += counter
        j += 1
        k += 1


def max_rank(L, l, r):
    if l < r:
        mid = l + (r - l) // 2
        max_rank(L, l, mid)
        max_rank(L, mid + 1, r)
        max_rank_merge(L, l, mid, r)


def depth(L):
    n = len(L)

    for i in range(n):
        L[i] = [L[i][0], L[i][1], 0]

    mergesort(L, 0, n - 1)
    max_rank(L, 0, n - 1)

    return max(L, key=lambda r: r[COUNT])[COUNT]


if __name__ == "__main__":
    L = [[1, 6],
         [5, 6],
         [2, 5],
         [8, 9],
         [1, 6]]

    print(depth(L))
