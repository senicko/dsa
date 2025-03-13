from random import randint


def merge(a, l, mid, r):
    # Find number of elements in the left and right subarray
    n_left = mid - l + 1
    n_right = r - mid

    # Copy values from left and right subarray for merge operation
    left = a[l:l + n_left]
    right = a[mid + 1:mid + 1 + n_right]

    i = 0
    j = 0
    k = l  # keep tract of insert position in original array

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


def merge_sort(a, l, r):
    # If subarray has more than one element
    if l < r:
        # Find midpoint
        q = (l + r) // 2

        # Sort sub arrays recursively
        merge_sort(a, l, q)
        merge_sort(a, q + 1, r)

        # Merge sorted sub arrays
        merge(a, l, q, r)


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    merge_sort(a, 0, len(a) - 1)

    # assert
    assert a == expected
    print(a, "OK")
