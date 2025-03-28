from random import randint
from math import inf


def min_max(T, l, r):
    found_min = inf
    found_max = -inf

    for i in range(l, r + 1, 2):
        j = i + 1

        if T[i] <= T[j]:
            if T[i] < found_min:
                found_min = T[i]
            if T[j] > found_max:
                found_max = T[j]
        else:
            if T[i] > found_max:
                found_max = T[i]
            if T[j] < found_min:
                found_min = T[j]

    return found_min, found_max


# O(n)
def partition(T, l, r):
    pivot_index = randint(l, r)
    T[pivot_index], T[r] = T[r], T[pivot_index]

    i = l - 1

    for j in range(l, r):
        if T[j] <= T[r]:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1


# O(n)
def quickselect(T, l, r, k):
    pivot = partition(T, l, r)

    if pivot == k:
        return pivot
    if pivot < k:
        return quickselect(T, pivot + 1, r, k)
    else:
        return quickselect(T, l, pivot - 1, k)


# O(n^2), ale dla bucket sorta z rozkładem jednostajnym O(1)
def insertion_sort(T):
    n = len(T)

    for i in range(n):
        key = T[i]
        j = i - 1

        while j >= 0 and T[j] > key:
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = key


# O(n) dla tablicy z wartościami z rozkładu jednostajnego.
def bucket_sort(T, l, r):
    n = r - l + 1
    buckets = [[] for _ in range(n)]

    min_v, max_v = min_max(T, l, r)
    span = max_v - min_v

    for i in range(l, r + 1):
        bucket_index = int(((T[i] - min_v) / span) * (n - 1))
        buckets[bucket_index].append(T[i])

    k = l

    for bucket in buckets:
        insertion_sort(bucket)

        for i in range(len(bucket)):
            T[k] = bucket[i]
            k += 1


def ogrodzenie(M, D, T):
    n = len(T)

    mid = quickselect(T, 0, n - 1, n // 2)
    bucket_sort(T, 0, mid - 1)
    bucket_sort(T, mid, n - 1)

    pairs_counter = 0
    for i in range(1, n):
        if T[i] - T[i - 1] >= D:
            pairs_counter += 1

    return pairs_counter
