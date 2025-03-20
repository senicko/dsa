"""
At every merge level we can keep track of number of "inversions" (defined in problem desc).
Every merge level keeps track of its own inversions.

At every call to merge inversions in left and right sub arrays were already 
counted in the deeper level of.
"""


def merge(A, l, mid, r):
    left_n = mid - l + 1
    right_n = r - mid

    left = A[l:l + left_n]
    right = A[mid + 1:mid + 1 + right_n]

    i = 0
    j = 0
    k = l
    less_count = 0

    while i < left_n and j < right_n:
        if left[i][0] < right[j][0]:
            A[k] = left[i]
            i += 1
            # Inc less elements counter
            less_count += 1
        else:
            A[k] = right[j]
            # Inc number of inversions
            right[j][1] += less_count
            j += 1
        k += 1

    while i < left_n:
        A[k] = left[i]
        i += 1
        k += 1

    while j < right_n:
        A[k] = right[j]
        # Inc number of inversions
        right[j][1] += less_count
        j += 1
        k += 1


def merge_sort(A, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(A, l, mid)
        merge_sort(A, mid + 1, r)
        merge(A, l, mid, r)


def maxrank(T):
    n = len(T)

    # Keep track of number of inversion for every element.
    for i in range(n):
        T[i] = [T[i], 0]

    merge_sort(T, 0, n - 1)
    return max(T, key=lambda x: x[1])[1]
