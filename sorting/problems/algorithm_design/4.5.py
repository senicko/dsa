from random import randint


# Solution with counting sort.
# Works great for small range of values.
def solve_counting_sort(a):
    n = len(a)
    max_value = max(a)
    min_value = min(a)
    buckets = [0 for _ in range(max_value)]

    for val in a:
        buckets[val - min_value] += 1

    max_value = a[0]

    for val in range(n):
        if buckets[max_value - min_value] < buckets[val - min_value]:
            max_value = val

    return max_value


def partition(a, l, r):
    # Select random pivot.
    pivot_index = randint(l, r)
    a[pivot_index], a[r] = a[r], a[pivot_index]

    # Continue standard Lomuto partition scheme.
    pivot = a[r]
    i = l - 1

    for j in range(l, r):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quicksort(a, l, r):
    while l < r:
        pivot = partition(a, l, r)

        if pivot - l < r - pivot:
            quicksort(a, l, pivot - 1)
            l = pivot + 1
        else:
            quicksort(a, pivot + 1, r)
            r = pivot - 1


def solve_sorting(a):
    n = len(a)

    # Sorting takes O(nlogn) time.
    quicksort(a, 0, n - 1)

    mode = 0
    max_count = 0
    current_count = 1

    # This scan takes O(n) time.
    for i in range(1, n):
        if a[i] != a[i - 1]:
            if current_count > max_count:
                mode = a[i - 1]
                max_count = current_count

            current_count = 1
        else:
            current_count += 1

    return mode


if __name__ == "__main__":
    a = [4, 6, 2, 4, 3, 1]
    assert solve_counting_sort(a) == solve_sorting(a)
