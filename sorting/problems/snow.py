def merge(a, l, mid, r):
    left = a[l:mid + 1]
    right = a[mid + 1:r + 1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(a, l, mid)
        merge_sort(a, mid + 1, r)
        merge(a, l, mid, r)


def snow(a):
    merge_sort(a, 0, len(a) - 1)

    day = 0
    total = 0

    for i in range(len(a)):
        if a[i] - day < 0:
            break

        total += a[i] - day
        day += 1

    return total


if __name__ == "__main__":
    a = [1, 7, 3, 4, 1]
    print(snow(a))
