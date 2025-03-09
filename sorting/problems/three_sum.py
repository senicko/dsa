"""
Three sum implementation without a Hash Map.
"""

from random import randint


def merge(a, l, mid, r):
    left_n = mid - l + 1
    right_n = r - mid

    left = a[l:l + left_n]
    right = a[mid + 1:mid + 1 + right_n]

    i = 0
    j = 0
    k = l

    while i < left_n and j < right_n:
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < left_n:
        a[k] = left[i]
        i += 1
        k += 1

    while j < right_n:
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l < r:
        mid = l + (r - l) // 2
        merge_sort(a, l, mid)
        merge_sort(a, mid + 1, r)
        merge(a, l, mid, r)


def two_sum(a, l, r, k):
    i = l
    j = r - 1

    while i < j:
        curr = a[i] + a[j]

        if curr == k:
            return True
        elif curr < k:
            i += 1
        else:
            j -= 1

    return False


"""
Pomysl:
    (1) Sortujemy tablice a.
    
    (2) Przechodzimy przez kazdy indeks i tablicy a. W prawej podtablicy wywolujemy two_sum dla
        wartosci k - a[i], ktory jednak nie musi sortowac tablicy a, poniewaz juz to zrobilismy w
        kroku (1), wiec dziala w czasie O(n).
        
Zlozonosc Czasowa:
    Sortowanie: O(nlogn)
    Przetworzenie: O(n^2)
    Razem: O(n^2)
"""


def three_sum(a, k):
    n = len(a)

    # (1)
    merge_sort(a, 0, n - 1)

    for i in range(n):
        # (2)
        if two_sum(a, i + 1, n, k - a[i]):
            return True

    return False


for _ in range(10):
    # arrange
    a = [randint(0, 99) for _ in range(10)]
    x = a[0]
    y = a[1]
    z = a[2]

    # test
    result = three_sum(a, x + y + z)

    # assert
    assert result is True
    print("\tOK")
