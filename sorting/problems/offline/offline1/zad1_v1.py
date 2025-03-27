from zad1testy import runtests

"""
Złożoność czasowa: O(NlogN)
    (1) O(N)
    (2) O(NlogN)
    (3) O(n)
"""

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


def build_heap(a):
    n = len(a)
    for i in range(parent(n - 1), -1, -1):
        heapify(a, n, i)


def heapsort(a):
    n = len(a)
    build_heap(a)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


def strong_string(T):
    n = len(T)

    # (1)
    for i in range(n):
        rev = T[i][::-1]
        if rev < T[i]:
            T[i] = rev

    # (2)
    heapsort(T)

    # (3)
    max_strength = 0
    current_strength = 1
    prev = T[0]

    for i in range(1, n):
        if T[i] == prev:
            current_strength += 1
        else:
            max_strength = max(max_strength, current_strength)
            current_strength = 1
            prev = T[i]

    return max(max_strength, current_strength)


# Odkomentuj by uruchomic duze testy
runtests(strong_string, all_tests=True)

# Zakomentuj gdy uruchamiasz duze testy
# runtests(strong_string, all_tests=False)
