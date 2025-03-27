from random import randint


# Lomuto's partition scheme.
def partition(a, l, r):
    i = l - 1

    for j in range(l, r):
        if a[j] <= a[r]:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[r] = a[r], a[i + 1]

    return i + 1


# Selects the k-th smallest index in unsorted array in O(n) time.
def quickselect(a, l, r, k):
    # k-th index should be present in the array.
    # We can handle this case in an arbitrary way.
    assert l <= k <= r

    # This also won't happen, if sought index exists.
    if l == r:
        return a[l]

    pivot_index = partition(a, l, r)

    # If pivot index is the sought index, return the found value.
    # If k is smaller than pivot index, search in left subarray.
    # If k is greater to pivot index, search in right subarray.

    if k == pivot_index:
        return a[k]
    elif k < pivot_index:
        return quickselect(a, l, pivot_index - 1, k)
    else:
        return quickselect(a, pivot_index + 1, r, k)


for _ in range(1):
    # arrange
    k = randint(0, 19)
    a = [randint(1, 9) for _ in range(10)]

    expected = sorted(a)[k]

    # test
    result = quickselect(a, 0, len(a) - 1, k)

    # assert
    assert expected == result
    print(expected, "=", result, "OK")
