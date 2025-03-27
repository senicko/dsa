"""
Proszę zaproponować algorytm, który mając na wejsciu tablicę A zwraca liczbę jej inwersji
(t.j, liczbę par indeksów i < j takich, że A[i] > A[j].)
"""


def merge(a, l, mid, r):
    inversions = 0

    left = a[l:mid + 1]
    right = a[mid + 1: r + 1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            inversions += len(left) - i
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        # We don't count any inversions here.
        # All inversions for smaller elements from right
        # subarray were already counted in the while above.

        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

    return inversions


def number_of_inversions(a, l, r):
    inv = 0

    if l < r:
        mid = (l + r) // 2
        inv += number_of_inversions(a, l, mid) + \
               number_of_inversions(a, mid + 1, r) + \
               merge(a, l, mid, r)

    return inv


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 1, 2]
    print(number_of_inversions(a, 0, len(a) - 1))
