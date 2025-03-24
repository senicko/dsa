from random import uniform


# Doing insertion sort this way (without swapping)
# reduces number of operations performed in the inner
# while loop.
def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] >= key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key


def bucket_sort(a):
    n = len(a)
    buckets = [[] for _ in range(n)]

    min_v = min(a)
    max_v = max(a)
    span = max_v - min_v + 1

    # Insert values to their buckets
    for v in a:
        bucket_index = int((v - min_v) / span * (n - 1))
        buckets[bucket_index].append(v)

    # Sort each bucket with insertion sort.
    for bucket in buckets:
        insertion_sort(bucket)

    # Insert sorted values back to a
    k = 0
    for bucket in buckets:
        for v in bucket:
            a[k] = v
            k += 1


for _ in range(20):
    # arrange
    a = [uniform(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    bucket_sort(a)

    # assert
    assert a == expected
    print(a, "ok")
