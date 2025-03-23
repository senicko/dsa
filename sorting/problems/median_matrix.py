"""
Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
"""

from random import randint


# Lomuto's partition scheme.
def partition(T, col, bottom, top):
    pivot = T[top][col]
    i = bottom - 1

    for j in range(bottom, top):
        if T[j][col] > pivot:
            i += 1
            T[i][col], T[j][col] = T[j][col], T[i][col]

    T[i + 1][col], T[top][col] = T[top][col], T[i + 1][col]
    return i + 1


# Quicksort algorithm using O(logn) memory
def quicksort(T, col, bottom, top):
    while bottom < top:
        pivot = partition(T, col, bottom, top)

        if pivot - bottom < top - pivot:
            quicksort(T, col, pivot + 1, top)
            top = pivot - 1
        else:
            quicksort(T, col, bottom, pivot - 1)
            bottom = pivot + 1


def median(T):
    n = len(T)

    for col in range(n):
        quicksort(T, col, 0, n - 1)


if __name__ == "__main__":
    n = randint(3, 6)
    T = []

    for i in range(n):
        T.append([randint(100, 999) for _ in range(n)])

    print("BEFORE=")
    print(*T, sep="\n")
    print()

    median(T)

    print("AFTER=")
    print(*T, sep="\n")
