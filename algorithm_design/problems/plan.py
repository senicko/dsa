from zad8testy import runtests
from queue import PriorityQueue


MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bounds(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def gather_oil(T, i, j, visited):
    n = len(T)
    m = len(T[0])

    if not in_bounds(i, j, n, m) or T[i][j] == 0 or visited[i][j]:
        return 0

    visited[i][j] = True
    total = T[i][j]

    for di, dj in MOVES:
        total += gather_oil(T, i + di, j + dj, visited)

    return total


def plan(T):
    n = len(T)
    m = len(T[0])

    visited = [[False] * m for _ in range(n)]
    oil = [0] * m

    for k in range(m):
        if T[0][k] != 0 and not visited[0][k]:
            oil[k] = gather_oil(T, 0, k, visited)

    reach = 0
    stops = 0

    while reach < m - 1:
        pq = PriorityQueue()

        for k in range(reach + 1):
            if oil[k] > 0:
                pq.put((-oil[k], k))

        tanked_oil, k = pq.get()
        tanked_oil *= -1

        oil[k] = 0
        reach += tanked_oil
        stops += 1

    return stops


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
