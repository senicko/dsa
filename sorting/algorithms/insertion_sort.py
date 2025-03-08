from random import randint


def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        # Note that initially j + 1 is just i, so the value we want to insert
        # at the valid spot.
        j = i - 1

        # Swap elements as long as value at a[j] is greater than value at a[j + 1]
        while j >= 0 and a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            j -= 1


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    insertion_sort(a)

    # assert
    assert a == expected
    print(a, "OK")

