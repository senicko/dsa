from random import randint


def merge(a, p, q, r):
    # Find number of elements in the left and right subarray
    n_left = q - p + 1
    n_right = r - q

    # Copy values from left and right subarray for merge operation
    left = a[p:p + n_left]
    right = a[q + 1:q + 1 + n_right]

    i = 0
    j = 0
    k = p  # keep tract of insert position in original array

    # While both pointers are not finished
    while i < n_left and j < n_right:
        # Choose smaller value and insert it to original array
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    # Make sure all values from left and right subarray
    # are inserted to original array.

    while i < n_left:
        a[k] = left[i]
        i += 1
        k += 1

    while j < n_right:
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a, p, r):
    # If subarray has more than one element
    if p < r:
        # Find midpoint
        q = (p + r) // 2

        # Sort sub arrays recursively
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)

        # Merge sorted sub arrays
        merge(a, p, q, r)


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    merge_sort(a)

    # assert
    assert a == expected
    print(a, "OK")
