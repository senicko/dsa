"""
`n` elementowa tablica `a` z liczbami ze zbioru 0 ... (n^2 - 1)
Trzeba posortować jak najszybciej.

Zauważamy, że mamy n elementów z zakresu n^2 - 1.
Możemy zapisać każdą liczbę w systemie N-kowym.
Gwarantuje nam to, że każda cyfra w naszej tablicy w systemie n-kowym ma
co najwyżej 2 cyfry. Korzystamy z Radix Sort'a korzystającego z counting sorta
do posortowania.
"""
from random import randint


def sort(a):
    n = len(a)
    a = counting_sort(a, key=lambda x: x % n)
    a = counting_sort(a, key=lambda x: x // 10)
    return a


def counting_sort(a, key):
    n = len(a)
    c = [0] * n
    b = [0] * n

    for i in range(n):
        c[key(a[i])] += 1

    for i in range(1, n):
        c[i] += c[i - 1]

    for i in range(n - 1, -1, -1):
        c[key(a[i])] -= 1
        b[c[key(a[i])]] = a[i]

    return b


if __name__ == "__main__":
    n = 10
    a = [randint(0, n ** 2 - 1) for _ in range(n)]
    a = sort(a)
    print(a)
