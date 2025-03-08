"""
Two sum implementation without Hash Map.

The "without Hash Map" is important here, as with it
this problem can be solved in O(n) time and O(n) space.
"""

from random import randint


def merge(a, l, q, r):
    left_n = q - l + 1
    right_n = r - q

    left = a[l:l + left_n]
    right = a[q + 1:q + 1 + right_n]

    i = 0
    j = 0
    k = l

    while i < left_n and j < right_n:
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < left_n:
        a[k] = left[i]
        i += 1
        k += 1

    while j < right_n:
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l < r:
        q = (l + r) // 2
        merge_sort(a, l, q)
        merge_sort(a, q + 1, r)
        merge(a, l, q, r)


def bin_search(a, l, r, v):
    if l <= r:
        mid = l + (r - l) // 2

        if a[mid] == v:
            return True
        elif v < a[mid]:
            return bin_search(a, l, mid - 1, v)
        else:
            return bin_search(a, mid + 1, r, v)
    else:
        return False


"""
Idea:
(1) Iterate through every value x.

(2) Search for value y after x so that x + y == k.
    By starting from index after x we won't process
    every pair twice.

Time Complexity: O(n^2)
"""


def two_sum_v1(a, k):
    n = len(a)

    # (1)
    for i in range(n):
        # (2)
        for j in range(i, n):
            if a[i] + a[j] == k:
                return True

    return False


"""
Idea: 
(1) Sort input array a.

(2) Iterate through every value x. 
    Search for k - x in the right sub array using binary search.
    We can ignore the left sub array, as we want to check every pair
    just once.
    
Time Complexity: O(nlogn)
"""


def two_sum_v2(a, k):
    n = len(a)

    # (1)
    merge_sort(a, 0, n - 1)

    # (2)
    for i in range(n):
        remainder = k - a[i]

        if bin_search(a, i + 1, n - 1, remainder):
            return True

    return False


"""
Idea: 
(1) Sort input array a.

(2) Maintain two pointers, left pointing to 0 and right pointing to n-1.
    Notice that our array is sorted, so incrementing left pointer increases
    the value, and similarly decrementing right decrements it.
    
    So while l<r we can check if our current pair is the sought one.
    If it's not than it's either too small or too big. We can modify
    out left and right pointers to descent to the solution.
    
(3) If l == r it means that we couldn't find a valid pair.

Time Complexity: O(nlogn)
"""


def two_sum_v3(a, k):
    n = len(a)

    # (1)
    merge_sort(a, 0, n-1)

    # (2)
    l = 0
    r = n - 1

    while l < r:
        total = a[l] + a[r]

        if total == k:
            return True
        elif total < k:
            l += 1
        else:
            r -= 1

    # (3)
    return False


for title, fn in [("Worst", two_sum_v1), ("Better", two_sum_v2), ("Best", two_sum_v3)]:
    print(title, end=" ")
    for _ in range(10):
        # arrange
        a = [randint(0, 99) for _ in range(10)]
        x = a[0]
        y = a[1]

        # test
        result = fn(a, x + y)

        # assert
        assert result is True
    print("\tOK")
