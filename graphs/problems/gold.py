from queue import PriorityQueue
from math import inf


def dijkstra(graph, s, converter=lambda x: x):
    n = len(graph)

    dist = [inf] * n
    parents = [0] * n
    queue = PriorityQueue()

    dist[s] = 0
    parents[s] = 0
    queue.put((dist[s], s))

    while not queue.empty():
        d, u = queue.get()

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            alt = d + converter(w)

            if dist[v] > alt:
                dist[v] = alt
                parents[v] = parents[u] + 1
                queue.put((alt, v))

    return dist, parents


def gold(G, V, s, t, r):
    n = len(G)

    # Distance to vertices before robbing any castle.
    dist_s, parents_s = dijkstra(G, s)

    # Distance to vertices after robbing a castle.
    dist_t, parents_t = dijkstra(G, t, converter=lambda x: 2 * x + r)

    min_dist = dist_s[t]

    for u in range(n):
        dist = dist_s[u] + dist_t[u] - V[u]
        min_dist = min(min_dist, dist)

    return min_dist
