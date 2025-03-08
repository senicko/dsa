from random import randint


# Hoare's partitioning algorithm.
def partition(a, l, r):
    # Pick the rightmost element as a pivot
    # and keep track of the highest index in the "low" subarray.
    pivot = a[r]
    i = l - 1

    # Note that we never reach index r, so pivot doesn't move during partitioning.
    for j in range(l, r):
        # If value a[j] belongs to the "low" subarray,
        # make it wider and move the value into it.
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    # Move pivot between "low" and "high" sub arrays.
    pivot_index = i + 1
    a[pivot_index], a[r] = a[r], a[pivot_index]

    return pivot_index


def quicksort(a, l, r):
    if l < r:
        pivot = partition(a, l, r)
        quicksort(a, l, pivot - 1)
        quicksort(a, pivot + 1, r)


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    quicksort(a)

    # assert
    assert a == expected
    print(a, "OK")
