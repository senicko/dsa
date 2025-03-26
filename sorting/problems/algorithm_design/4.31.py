# Binary search for an arbitrary value in array of integers
# shifted by k positions right.
def k_binary_search(a, k, x):
    n = len(a)

    l = k
    r = n - 1 + k

    while l <= r:
        mid = l + (r - l) // 2

        if a[mid % n] == x:
            return mid % n
        elif a[mid % n] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1


# Searches for max element in sorted array with
# values shifted by k indexes in O(nlogn) time.
def binary_max(a):
    n = len(a)

    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if a[mid] > a[(mid + 1) % n]:
            return a[mid]

        elif a[mid] >= a[l]:
            l = mid + 1
        else:
            r = mid - 1

    return None


if __name__ == "__main__":
    a = [29, 35, 42, 5, 15, 27]
    print(binary_max(a))
