from random import randint


def selection_sort(a):
    n = len(a)

    for i in range(n):
        min_j = i

        for j in range(i + 1, n):
            if a[j] < a[min_j]:
                min_j = j

        a[i], a[min_j] = a[min_j], a[i]


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    selection_sort(a)

    # assert
    assert a == expected
    print(a, "OK")
