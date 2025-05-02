def topological_sort(graph):
    n = len(graph)
    order = []
    visited = [False] * n

    def dfs_visit(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                dfs_visit(u)
        order.append(v)

    for v in range(n):
        if not visited[v]:
            visited[v] = True
            dfs_visit(v)

    order.reverse()
    return order


def is_hamiltonian(graph):
    n = len(graph)
    topological_order = topological_sort(graph)

    for i in range(n - 1):
        if not topological_order[i + 1] in graph[topological_order[i]]:
            return False

    return True


if __name__ == "__main__":
    graph = [[1], [2], [3], [4], []]
    print(is_hamiltonian(graph))
