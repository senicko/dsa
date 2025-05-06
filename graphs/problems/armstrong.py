"""
Kiedy przetwarzamy rower, interesuje nas odległość od s do roweru
i odległość z roweru do t, czyli odległość z t do roweru.
"""

from queue import PriorityQueue
from math import inf, floor


def build_graph(edges):
    n = max(map(lambda x: max(x[0], x[1]), edges)) + 1
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


def dijkstra(graph, s):
    n = len(graph)

    dist = [inf] * n
    queue = PriorityQueue()

    dist[s] = 0
    queue.put((0, s))

    while not queue.empty():
        d, u = queue.get()

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            alt = dist[u] + w
            if dist[v] > alt:
                dist[v] = alt
                queue.put((alt, v))

    return dist


def armstrong(B, G, s, t):
    graph = build_graph(G)

    dist_s_t = dijkstra(graph, s)
    dist_t_s = dijkstra(graph, t)

    result = dist_s_t[t]

    for u, p, q in B:
        result = min(result, dist_s_t[u] + dist_t_s[u] * (p / q))

    return floor(result)


runtests(armstrong, all_tests=True)
