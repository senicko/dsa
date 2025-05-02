def build_graph(edges):
    n = max(edges, key=lambda e: max(e[0], e[1]))
    n = max(n[0], n[1]) + 1

    graph = [[] for _ in range(n)]

    for u, v, p in edges:
        graph[u].append((v, p))
        graph[v].append((u, p))

    return graph


def flight(L, x, y, t):
    graph = build_graph(L)
    n = len(graph)

    def dfs_visit(u, min_p, max_p, visited):
        if u == y:
            return

        for v, p in graph[u]:
            if not visited[v] and p - t <= max_p and p + t >= min_p:
                visited[v] = True
                dfs_visit(v, max(min_p, p - t), min(max_p, p + t), visited)

    for u, p in graph[x]:
        visited = [False] * n
        visited[x] = visited[u] = True

        dfs_visit(u, p - t, p + t, visited)

        if visited[y]:
            return True

    return False
