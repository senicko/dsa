from random import randint

'''
(1) Store number of elements equal to
    x at index x in array count.

(2) Store number of elements less than or equal
    to x in at position x in array count.

(3) At this point we have an array count which stores number of elements
    less than or equal to x, where x is the index. So count[200] = 100
    means that there are 100 elements less than or equal to 200.


(4) Find how many elements less than or equal to a[i] there are,
    and insert a[i] to the index after them (excluding itself).
    So if we have count[200] = 100, then we want to insert 200 
    at index 99 (100'th position)
'''


def counting_sort(a, n, limit):
    out = [0 for _ in range(n)]
    count = [0 for _ in range(limit + 1)]

    # (1)
    for i in range(n):
        count[a[i]] += 1

    # (2)
    for i in range(1, limit + 1):
        count[i] = count[i] + count[i - 1]

    # (3)

    # (4)
    for i in range(n - 1, -1, -1):
        out[count[a[i]] - 1] = a[i]
        count[a[i]] -= 1

    return out


for _ in range(20):
    # arrange
    a = [randint(100, 999) for _ in range(15)]
    expected = sorted(a)

    # test
    a = counting_sort(a, len(a), max(a))

    # assert
    assert a == expected
    print(a, "ok")
