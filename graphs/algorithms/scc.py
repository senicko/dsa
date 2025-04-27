def build_transpose(graph):
    n = len(graph)
    new = [[] for _ in range(n)]

    for u in range(n):
        for v in graph[u]:
            new[v].append(u)

    return new


def get_order(graph):
    n = len(graph)
    visited = [False] * n
    order = []

    for u in range(n):
        if not visited[u]:
            visited[u] = True
            dfs_visit(graph, visited, u, order)

    order.reverse()
    return order


def dfs_visit(graph, visited, v, out):
    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            dfs_visit(graph, visited, u, out)

    out.append(v)


def extract_components(graph, order):
    n = len(graph)
    visited = [False] * n

    components = []

    for u in order:
        if not visited[u]:
            visited[u] = True
            component = []
            dfs_visit(graph, visited, u, component)
            components.append(component)

    return components


def scc(graph):
    order = get_order(graph)
    transpose = build_transpose(graph)
    return extract_components(transpose, order)


if __name__ == "__main__":
    graph = [
        [1],
        [2, 6, 5],
        [3],
        [4, 2],
        [4],
        [0, 2],
        [3, 7],
        [4, 6]
    ]

    print(scc(graph))
