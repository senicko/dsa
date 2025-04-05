from random import random, randint


def merge(a, l, mid, r):
    left = a[l:mid + 1]
    right = a[mid + 1:r + 1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l < r:
        mid = l + (r - l) // 2
        merge_sort(a, l, mid)
        merge_sort(a, mid + 1, r)
        merge(a, l, mid, r)


def right_bound(a, x):
    n = len(a)

    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if a[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1

    return l


def union(a, b):
    n = len(a)

    merge_sort(a, 0, n - 1)
    merge_sort(b, 0, n - 1)
    union = []

    i = 0
    j = 0

    while i < n and j < n:
        if a[i] == b[j]:
            union.append(a[i])
            i = right_bound(a, a[i])
            j = right_bound(b, b[j])
        elif a[i] < b[j]:
            union.append(a[i])
            i = right_bound(a, a[i])
        else:
            union.append(b[j])
            j = right_bound(b, b[j])

    while i < n:
        union.append(a[i])
        i = right_bound(a, a[i])

    while j < n:
        union.append(b[j])
        j = right_bound(b, b[j])

    return union


if __name__ == "__main__":
    a = [randint(1, 10) for _ in range(20)]
    b = [randint(30, 40) for _ in range(20)]
    print(union(a, b))
