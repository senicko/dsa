"""
Proszę zaproponować algorytm, który mając na wejsciu tablicę A zwraca liczbę jej inwersji
(t.j, liczbę par indeksów i < j takich, że A[i] > A[i].)
"""


def merge(a, l, mid, r):
    left_n = mid - l + 1
    right_n = r - mid
    inversions = 0

    left = a[l:l + left_n]
    right = a[mid + 1:mid + 1 + right_n]

    i = 0
    j = 0
    k = l

    while i < left_n and j < right_n:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            inversions += left_n - i
            a[k] = right[j]
            j += 1
        k += 1

    while i < left_n:
        a[k] = left[i]
        i += 1
        k += 1

    while j < right_n:
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
