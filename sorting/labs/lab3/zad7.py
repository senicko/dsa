"""
Znaleźć k-ty element
"""
from random import randint


# Lomuto's partition scheme.
def partition(T, l, r):
    pivot = T[r]
    i = l - 1

    for j in range(l, r):
        if T[j] < pivot:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quickselect(T, l, r, k):
    if l == r:
        # In this case there might not be kth element.
        return T[l]

    pivot = partition(T, l, r)

    if pivot == k:
        return T[pivot]
    elif k > pivot:
        return quickselect(T, pivot + 1, r, k)
    else:
        return quickselect(T, l, pivot - 1, k)


for _ in range(20):
    # arrange
    k = randint(0, 19)
    a = [randint(10, 99) for _ in range(20)]
    expected = sorted(a)[k]

    # test
    result = quickselect(a, 0, len(a) - 1, k)

    # assert
    assert expected == result
    print(expected, "=", result, "OK")
