"""
Note that we are working with logarithms.
Summing them works like multiplication.

-loga > 0 for a < 0
-loga < 0 for a > 0

After replacing weights with those values,
we can search for a negative weight cycle
using standard Bellman-Ford algorithm.
"""

from math import inf, log


def currency_glitch(graph):
    n = len(graph)

    # Map weights to -log(w) and add dummy node with
    # directed edges to all the other vertices of weight 1.

    for u in range(n):
        graph[u].append(0)
        for v in range(n):
            graph[u][v] = -log(graph[u][v])

    n += 1
    graph.append([0] * n)

    # Work

    dist = [inf] * n
    dist[n - 1] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                alt = dist[u] + graph[u][v]

                if dist[v] > alt:
                    dist[v] = alt

    # Validate

    for u in range(n):
        for v in range(n):
            if dist[v] > dist[u] + graph[u][v]:
                # Yes, there exists such currency, as we've found
                # negative weight cycle.
                return True

    # No, there's no such currency.
    return False


if __name__ == "__main__":
    exchange_rates = [
        [1.0, 0.9, 1.1, 1.25, 0.8, 0.95],
        [1.1111, 1.0, 1.2222, 1.3889, 0.8889, 1.0556],
        [0.9091, 0.8182, 1.0, 1.1364, 0.7273, 0.8636],
        [0.8, 0.72, 0.88, 1.0, 0.64, 0.76],
        [1.25, 1.125, 1.375, 1.5625, 1.0, 1.1875],
        [1.0526, 0.9474, 1.1579, 1.3158, 0.8421, 1.0]
    ]

    print(currency_glitch(exchange_rates))
