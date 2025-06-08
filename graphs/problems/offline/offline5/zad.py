from zadtesty import runtests
from collections import deque
from math import inf


def goodknight(G, s, t):
    n = len(G)

    # We need to duplicate every vertex 17 times, so that
    # we can visit every vertex with different stamina levels.
    dist = [[inf] * 17 for _ in range(n)]

    buckets = [deque() for _ in range(16 * n + 1)]

    buckets[0].append((s, 16))
    dist[s] = [0] * 17

    d = 0

    while True:
        # Find next not empty bucket.
        # This while does O(C * n) iterations.
        while not buckets[d] and d < 16 * n:
            d += 1

        # Stop if we have processed all buckets.
        if d == 16 * n:
            break

        # This pop() can happen O(V) times, so in our case O(n)
        # (all of the vertices can be in the same bucket)
        u, stamina = buckets[d].pop()

        # Skip stale vertices.
        if d > dist[u][stamina]:
            continue

        # Relax every edge.
        # This while does O(E) iterations, so in our case O(n)
        for v in range(n):
            if G[u][v] == -1:
                continue

            w = G[u][v]

            # Simulate sleeping in a castle.
            # We can't go longer than 16 hours.
            # Sleeping at a castle resets stamina,
            # but adds 8 to the weight. Edge weights
            # are from 1 to 8, but sleeping makes it 1 - 16.

            real_w = w
            real_stamina = stamina

            if real_w > real_stamina:
                real_stamina = 16
                real_w += 8

            real_stamina -= w
            alternative = d + real_w

            if dist[v][real_stamina] > alternative:
                dist[v][real_stamina] = alternative
                buckets[alternative].append((v, real_stamina))

    return min(dist[t])


runtests(goodknight, all_tests=True)
