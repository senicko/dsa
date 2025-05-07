from math import inf


def articulation_points(graph):
    n = len(graph)

    time = 0
    visited = [False] * n
    low = [inf] * n
    discovery = [inf] * n
    points = set()

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
                    points.add(u)
            elif parent != v:
                low[u] = min(low[u], discovery[v])

        return children

    for u in range(n):
        if not visited[u]:
            if dfs_visit(u) >= 2:
                points.add(u)

    return points


def koleje(B):
    n = max(map(lambda x: max(x[0], x[1]), B)) + 1

    graph = [[] for _ in range(n)]

    for u, v in B:
        graph[u].append(v)
        graph[v].append(u)

    return len(articulation_points(graph))
