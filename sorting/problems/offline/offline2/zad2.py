"""
Sebastian Flajszer

Złożoność czasowa: O(nlogn)

Opis:
    (1) Do zliczania wykorzystujemy działanie algorytmu merge sort. Inwersje możemy
        wykryć podczas operacji merge, kiedy element z tablicy right jest mniejszy od
        elementu z tablicy left. Właśnie te sytuacje zliczamy dla każdego poziomu wywołania
        merge. Na każdym poziomie wywołania merge zliczamy tylko i wyłącznie inwersje na tym poziomie,
        ponieważ inwersje na głębszych poziomach rekurencji zostały już policzone.
"""

from zad2testy import runtests


def merge(A, l, mid, r):
    inversions = 0

    left_n = mid - l + 1
    right_n = r - mid

    left = A[l:l + left_n]
    right = A[mid + 1:mid + 1 + right_n]

    i = 0
    j = 0
    k = l

    while i < left_n and j < right_n:
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
            inversions += left_n - i
        k += 1

    while i < left_n:
        A[k] = left[i]
        i += 1
        k += 1

    while j < right_n:
        A[k] = right[j]
        j += 1
        k += 1

    return inversions


def merge_sort(A, l, r):
    inv = 0

    if l < r:
        mid = (l + r) // 2
        inv += merge_sort(A, l, mid) + merge_sort(A, mid + 1, r) + merge(A, l, mid, r)

    return inv


def count_inversions(A):
    return merge_sort(A, 0, len(A) - 1)


# Odkomentuj by uruchomic duze testy
runtests(count_inversions, all_tests=True)

# Zakomentuj gdy uruchamiasz duze testy
# runtests(count_inversions, all_tests=False)
