from math import inf


def find_bridges(graph):
    n = len(graph)
    bridges = []

    time = 0
    visited = [False] * n
    discovery = [0] * n
    low = [inf] * n

    def dfs_visit(u, parent=-1):
        nonlocal time

        visited[u] = True
        # Init low[v] with discover time.
        time += 1
        low[u] = discovery[u] = time

        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v, u)

                # Can v reach vertex with discovery
                # time lower than low[v]?

                low[u] = min(low[u], low[v])

                # If lowest discovery time reachable by v is
                # greater than discovery[v], {v, v} is a bridge.

                if low[v] > discovery[u]:
                    bridges.append((u, v))
            elif v != parent:
                # Does the vertex to which we have found
                # a back edge has lower discovery time?
                low[u] = min(low[u], discovery[v])

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return bridges


if __name__ == "__main__":
    graph = [
        [1],
        [0, 2],
        [1, 3, 4],
        [2, 4],
        [3, 2]
    ]

    print(find_bridges(graph))
