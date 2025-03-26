from random import randint

N = 0


# Lomuto's partition scheme.
def partition(T, l, r):
    pivot = T[r]
    i = l - 1

    for j in range(l, r):
        if T[j] <= pivot:
            i += 1
            T[j], T[i] = T[i], T[j]

    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def select(T, l, r, k):
    if l >= r:
        return -1

    pivot = partition(T, l, r)

    if pivot == k:
        return
    elif pivot < k:
        return select(T, pivot + 1, r, k)
    else:
        return select(T, l, pivot - 1, k)


def median(T):
    global N
    N = len(T)

    tmp = [0] * (N * N)

    for i in range(N):
        for j in range(N):
            tmp[N * i + j] = T[i][j]

    start = (N * N - N) // 2
    end = start + N

    for i in range(start, end):
        select(tmp, 0, N * N - 1, i)

    i = 0

    for x in range(0, N - 1):
        for y in range(x + 1, N):
            T[y][x] = tmp[i]
            T[x][y] = tmp[end + i]
            i += 1

    for y in range(N):
        T[y][y] = tmp[i]
        i += 1


if __name__ == "__main__":
    T = [
        [12, 25, 38, 41, 54, 67, 72, 89],
        [15, 28, 39, 42, 55, 68, 73, 90],
        [18, 31, 40, 45, 56, 69, 74, 91],
        [21, 34, 43, 46, 57, 70, 75, 92],
        [24, 37, 44, 49, 58, 71, 76, 93],
        [27, 48, 50, 52, 60, 77, 80, 95],
        [30, 51, 53, 62, 78, 81, 85, 97],
        [33, 59, 61, 66, 79, 82, 88, 99]
    ]

    median(T)
    print(*T, sep="\n")
