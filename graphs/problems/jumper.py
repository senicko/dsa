from math import inf
from queue import PriorityQueue


def jumper(G, s, w):
    print(*G, sep='\n')

    n = len(G)

    dist = [[inf] * 2 for _ in range(n)]
    queue = PriorityQueue()

    dist[s][False] = 0
    queue.put((dist[s][False], s, False))

    while not queue.empty():
        d, u, used_boots = queue.get()

        # Don't process already visited
        # vertices twice.
        if d > dist[u][used_boots]:
            continue

        for v in range(n):
            if G[u][v] == 0:
                continue

            new_dist = d + G[u][v]

            if dist[v][False] > new_dist:
                dist[v][False] = new_dist
                queue.put((dist[v][False], v, False))

            # If we've used boots to reach u,
            # we can't use them again.
            if used_boots:
                continue

            for k in range(n):
                if G[v][k] == 0:
                    continue

                vk = max(G[u][v], G[v][k])
                new_dist = d + vk

                if dist[k][True] > new_dist:
                    dist[k][True] = new_dist
                    queue.put((dist[k][True], k, True))

    return min(dist[w])
