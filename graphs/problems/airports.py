from queue import PriorityQueue
from math import inf


def airports(G, A, s, t):
    n = len(G)
    G.append([])

    # Create "air" vertex, that connects airports.
    for u in range(n):
        G[u].append((n, A[u]))
        G[n].append((u, A[u]))

    n += 1
    dist = [inf] * n
    queue = PriorityQueue()

    dist[s] = 0
    queue.put((dist[s], s))

    while not queue.empty():
        d, u = queue.get()

        if d > dist[u]:
            continue

        for v, w in G[u]:
            alternative = d + w

            if dist[v] > alternative:
                dist[v] = alternative
                queue.put((alternative, v))

    return dist[t]
