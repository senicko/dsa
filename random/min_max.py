from math import inf
from random import randint


# Finds minimum and maximum of an array in O((3/2)*n) time complexity.
def min_max(a):
    n = len(a)

    found_min = inf
    found_max = -inf

    for i in range(0, n, 2):
        j = i + 1

        # In each iteration we make 3 comparisons.
        # Because of that we will make ((1/2)*n)*3 comparisons, so (3/2)*n

        if a[i] <= a[j]:
            if a[i] < found_min:
                found_min = a[i]
            if a[j] > found_max:
                found_max = a[j]
        else:
            if a[i] > found_max:
                found_max = a[i]
            if a[j] < found_min:
                found_min = a[j]

    return found_min, found_max


for _ in range(20):
    # arrange
    a = [randint(0, 420) for _ in range(10)]
    expected_min, expected_max = min(a), max(a)

    # test
    found_min, found_max = min_max(a)

    # assert
    assert found_min == expected_min and found_max == expected_max
    print("OK")
