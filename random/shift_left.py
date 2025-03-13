def shift_left(a, k):
    n = len(a)

    # It doesn't make sense to shift array by itself
    assert k < n

    for i in range(k):
        a[i], a[i + k] = a[i + k], a[i]

    left = n - 2 * k
    counter = 0

    while counter < left:
        for i in range(n - left + counter, k + counter, -1):
            a[i], a[i - 1] = a[i - 1], a[i]

        counter += 1
