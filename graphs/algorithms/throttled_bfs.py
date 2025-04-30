from collections import deque
from math import inf


def throttled_bfs(graph, s):
    n = len(graph)
    dist = [inf] * n

    queue = deque()
    queue.append((s, 0, 0))

    while queue:
        u, steps, journey = queue.popleft()

        if dist[u] > journey:
            continue

        if steps != 0:
            queue.append((v, steps - 1, journey))
            continue

        for v, w in graph[u]:
            new_journey = journey + w

            if dist[v] > new_journey:
                dist[v] = new_journey
                queue.append((v, w - 1, new_journey))

    return dist
