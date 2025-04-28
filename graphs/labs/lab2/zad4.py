def compute_finish_order(graph):
    n = len(graph)
    visited = [False] * n
    order = []

    def dfs_visit(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                dfs_visit(u)
        order.append(v)

    for v in range(n):
        if not visited[n]:
            visited[v] = True
            dfs_visit(v)

    order.reverse()
    return order


def scc(graph):
    finish_order = compute_finish_order(graph)

    n = len(graph)
    visited = [False] * n

    def dfs_visit(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                dfs_visit(u)

    for v in finish_order:
        if not visited[v]:



