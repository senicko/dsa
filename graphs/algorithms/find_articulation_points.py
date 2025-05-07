from math import inf


def find_articulation_points(graph):
    n = len(graph)

    time = 0
    low = [inf] * n
    discovery = [inf] * n
    visited = [False] * n
    points = [False] * n

    def dfs_visit(u, parent=None):
        nonlocal time

        time += 1
        visited[u] = True
        low[u] = discovery[u] = time
        children = 0

        for v in graph[u]:
            if not visited[v]:
                children += 1
                dfs_visit(v, u)
                low[u] = min(low[u], low[v])

                if parent is not None and low[v] >= discovery[u]:
                    points[u] = True
            elif parent != v:
                low[u] = min(low[u], discovery[v])

        if parent is None and children >= 2:
            points[u] = True

    for u in range(n):
        if not visited[u]:
            dfs_visit(u)

    return points


if __name__ == "__main__":
    graph = [
        [1, 2],
        [0, 2, 3],
        [0, 1],
        [1, 4],
        [3]
    ]

    print(find_articulation_points(graph))
