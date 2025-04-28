from zad4testy import runtests
from queue import PriorityQueue
from math import inf


def dijkstra(n, graph, a):
    dist = [inf] * n
    visited = [False] * n
    queue = PriorityQueue()

    dist[a] = 0
    queue.put((0, a))

    while not queue.empty():
        v_dist, v = queue.get()

        if visited[v]:
            continue

        visited[v] = True

        for u, t in graph[v]:
            if not visited[u] and dist[u] > dist[v] + t:
                dist[u] = dist[v] + t
                queue.put((dist[u], u))

    return dist


def spacetravel(n, E, S, a, b):
    graph = [[] for _ in range(n + 1)]

    for u, v, t in E:
        graph[u].append((v, t))
        graph[v].append((u, t))

    for v in S:
        graph[n].append((v, 0))
        graph[v].append((n, 0))

    distances = dijkstra(n + 1, graph, a)

    return distances[b] if distances[b] != inf else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
