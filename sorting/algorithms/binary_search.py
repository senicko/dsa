# Searches for a value in O(n * log(n)).
def binary_search(a, k):
    n = len(a)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == k:
            return mid
        elif a[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Finds the first index equal to k.
def left_bound(a, k):
    n = len(a)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        # Because of < operator we'll
        # move to the left boundary.
        if a[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Finds the first index greater than k.
def right_bound(a, k):
    n = len(a)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        # Because of <= operator we'll
        # move to the right boundary.
        if a[mid] <= k:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Counts occurrences of an element in O(n * log(n))
def binary_count(a, k):
    return right_bound(a, k) - left_bound(a, k)


if __name__ == "__main__":
    a = [2, 2, 2, 2, 4, 5, 5]
    print(a)
    print(binary_count(a, 2))
    print(binary_search(a, 4))
