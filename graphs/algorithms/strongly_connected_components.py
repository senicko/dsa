from math import inf


class PriorityQueueEntry(object):
    def __init__(self, priority, value):
        self.priority = priority
        self.data = value

    def __lt__(self, other):
        return self.priority < other.priority


def build_transpose(graph):
    n = len(graph)
    transpose = [[] for _ in range(n)]

    for v in range(n):
        for neighbour in graph[v]:
            transpose[neighbour].append(v)

    return transpose


def compute_finish_order(graph):
    n = len(graph)
    time = 0
    visited = [False] * n
    finish_order = []

    def dfs_visit(v):
        nonlocal time
        time += 1

        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                dfs_visit(u)

        time += 1
        # Append vertex to finish_order array after processing.
        # Note that vertices will be ordered in ascending order.
        finish_order.append(v)

    for v in range(n):
        if not visited[v]:
            visited[v] = True
            dfs_visit(v)

    return finish_order


def extract_components(graph, finish_times):
    n = len(graph)
    components = []
    visited = [False] * n

    def dfs_visit(v):
        for u in graph[v]:
            if not visited[u]:
                components[-1].append(u)
                visited[u] = True
                dfs_visit(u)

    # Process vertices in descending order of
    # their discovery times.
    for i in range(len(finish_times) - 1, -1, -1):
        v = finish_times[i]

        if not visited[v]:
            components.append([v])
            visited[v] = True
            dfs_visit(v)

    return components


def strongly_connected_components(graph):
    finish_order = compute_finish_order(graph)
    transpose = build_transpose(graph)
    return extract_components(transpose, finish_order)


if __name__ == "__main__":
    graph = [[1], [2, 6, 5], [3], [4, 2], [4], [0, 2], [3, 7], [4, 6]]
    print(strongly_connected_components(graph))
