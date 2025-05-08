from collections import deque
from math import inf, isinf


def mykoryza(G, T, d):
    n = len(G)

    queue = deque()
    dist = [inf] * n

    for m in range(len(T)):
        u = T[m]
        dist[u] = m
        queue.append(u)

    count = 1

    while queue:
        u = queue.popleft()

        for v in G[u]:
            if isinf(dist[v]):
                if dist[u] == d:
                    count += 1

                dist[v] = dist[u]
                queue.append(v)

    return count
