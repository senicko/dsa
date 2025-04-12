from math import inf


def find_bridges(graph):
    n = len(graph)
    bridges = []

    time = 0
    visited = [False] * n

    low = [inf] * n
    discovery = [0] * n

    def dfs_visit(v, parent=-1):
        nonlocal discovery, visited, time

        time += 1

        # (1)   Init low[v] with discover time.
        low[v] = discovery[v] = time

        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                dfs_visit(u, v)

                # (2)   Can u reach vertex with discovery
                #       time lower than low[v]?
                low[v] = min(low[v], low[u])

                # (4)   If lowest discovery time reachable by u is
                #       greater than discovery[v], {v, u} is a bridge.
                if low[u] > discovery[v]:
                    bridges.append((v, u))
            elif u != parent:
                # (3)   Does the vertex to which we have found
                #       a back edge has lower discovery time?
                low[v] = min(low[v], discovery[u])

    for v in range(n):
        if not visited[v]:
            visited[v] = True
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
