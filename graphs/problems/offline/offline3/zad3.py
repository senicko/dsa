"""
Z reguły mnożenia (kombinatoryka)

- x = ilość najkrótszych ścieżek z t do u
- y = ilość najkrótszych ścieżek z s do v
- x * y = ilość ścieżek przechodzących przez krawędź u--v

Jeżeli x * y == ilości najkrótszych ścieżek z t do s,
to najkrótsza ścieżka musi przejść przez u--v.

Z tego powodu u--v to "most" w grafie najkrótszych ścieżek.
Usunięcie u--v musi spowodować wydłużenie najkrótszej ścieżki.
"""

from zad3testy import runtests
from collections import deque
from math import inf


def bfs(G, start):
    n = len(G)

    visited = [False] * n
    distances = [inf] * n
    parents = [None] * n
    counts = [0] * n

    visited[start] = True
    distances[start] = 0
    counts[start] = 1

    queue = deque([start])

    while queue:
        v = queue.pop()

        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                parents[u] = v
                distances[u] = distances[v] + 1
                counts[u] = counts[v]
                queue.appendleft(u)
            elif distances[v] + 1 == distances[u]:
                counts[u] += counts[v]

    return counts, parents


def longer(G, s, t):
    counts_s_t, parents = bfs(G, s)
    counts_t_s, _ = bfs(G, t)

    shortest = []
    curr = t

    while curr is not None:
        shortest.append(curr)
        curr = parents[curr]

    total_shortest_s_t = counts_s_t[t]

    for i in range(len(shortest) - 1):
        u = shortest[i]
        v = shortest[i + 1]

        if counts_t_s[u] * counts_s_t[v] == total_shortest_s_t:
            return shortest[i + 1], shortest[i]

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
