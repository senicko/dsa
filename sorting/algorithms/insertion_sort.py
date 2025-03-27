from random import randint


def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] >= key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    insertion_sort(a)

    # assert
    assert a == expected
    print(a, "OK")
