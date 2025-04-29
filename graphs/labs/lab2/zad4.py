def transpose(graph):
    n = len(graph)
    new_graph = [[] for _ in range(n)]

    for u in range(n):
        for v in graph[u]:
            new_graph[v].append(u)

    return new_graph


def dfs_visit(u, graph, visited, out):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            dfs_visit(v, graph, visited, out)

    out.append(u)


def get_finish_order(graph):
    n = len(graph)
    visited = [False] * n
    finish_order = []

    for u in range(n):
        if not visited[u]:
            visited[u] = True
            dfs_visit(u, graph, visited, finish_order)

    return reversed(finish_order)


def extract_components(graph, finish_order):
    n = len(graph)
    visited = [False] * n
    components = []

    for u in finish_order:
        if not visited[u]:
            visited[u] = True
            components.append([])
            dfs_visit(u, graph, visited, components[-1])

    return components


def scc(graph):
    finish_order = get_finish_order(graph)
    transposed = transpose(graph)
    return extract_components(transposed, finish_order)
