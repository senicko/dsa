"""
Quick sort używając max log(n) dodatkowej pamięci.
"""

from random import randint


# Lomuto's partition scheme.
def partition(A, l, r):
    pivot = A[r]
    i = l - 1

    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]

    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


def quicksort(A, l, r):
    # (1)
    # Usuwamy rekurencję ogonową, wykorzystując pętlę
    # zamiast ifa. Dzięki temu quicksort robi 2 razy mniej
    # wywołań rekurencyjnych. Ta optymalizacja nie gwarantuje jeszcze pamięci `O(nlogn)`.
    while l < r:
        pivot = partition(A, l, r)

        # (2)
        # Po wybraniu pivot'a mniejszy przedział chcemy obsłużyć wywołaniem rekurencyjnym,
        # a większy przedział iteracyjnie dzięki pętli while.
        # To zagwarantuje nam zużycie pamięci `O(logn)`, ponieważ w najgorszym przypadku, kiedy
        # oba przedziały będą równej długości, zrobimy `logn` wywołań rekurencyjnych.

        if pivot - l < r - pivot:
            # Jeżeli lewy przedział jest mniejszy niż prawy przedział.
            quicksort(A, l, pivot - 1)
            l = pivot + 1
        else:
            quicksort(A, pivot + 1, r)
            r = pivot - 1


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    quicksort(a, 0, len(a) - 1)

    # assert
    assert a == expected
    print(a, "OK")
