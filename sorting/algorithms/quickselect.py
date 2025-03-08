from random import randint


def partition(a, l, r):
    pivot = a[r]
    i = l - 1

    for j in range(l, r):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    pivot_index = i + 1
    a[pivot_index], a[r] = a[r], a[pivot_index]

    return pivot_index


# Selects the k-th smallest index in unsorted array in O(n) time.
def quickselect(a, k, l, r):
    # k-th index should be present in the array.
    # We can handle this case in arbitrary way.
    assert l <= k <= r

    if l == r:
        return a[l]

    pivot_index = partition(a, l, r)

    # If pivot index is the sought index, return the found value.
    # If k is smaller than pivot index, search in left subarray.
    # If k is greater or equal to pivot index, search in right subarray.

    if k == pivot_index:
        return a[k]
    elif k < pivot_index:
        return quickselect(a, k, l, pivot_index - 1)
    else:
        return quickselect(a, k, pivot_index + 1, r)


for _ in range(20):
    # arrange
    k = randint(0, 19)
    a = [randint(10, 99) for _ in range(20)]
    expected = sorted(a)[k]

    # test
    result = quickselect(a, k, 0, len(a) - 1)

    # assert
    assert expected == result
    print(expected, "=", result, "OK")
