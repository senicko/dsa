from zadtesty import runtests
from collections import deque
from math import inf


def goodknight(G, s, t):
    n = len(G)

    dist = [[inf] * 17 for _ in range(n)]
    queue = deque()

    dist[s] = [0] * 17
    # (u, distance at u, steps left to reach u, stamina at u)
    queue.append((s, dist[s][0], 0, 16))

    while queue:
        u, d, steps, stamina = queue.popleft()

        # If we've processed u with better
        # distance before, we can ignore this case.
        if d > dist[u][stamina]:
            continue

        # If we didn't reach u yet, continue our journey.
        if steps != 0:
            queue.append((u, d, steps - 1, stamina))
            continue

        for v in range(n):
            # If u and v aren't connected.
            if G[u][v] == -1:
                continue

            w = G[u][v]
            real_w = w
            real_stamina = stamina

            # Consider sleeping.
            if w > stamina:
                real_w += 8
                real_stamina = 16

            real_stamina -= w
            alternative = d + real_w

            if dist[v][real_stamina] > alternative:
                dist[v][real_stamina] = alternative
                queue.append((v, alternative, real_w - 1, real_stamina))

    return min(dist[t])


runtests(goodknight, all_tests=True)
