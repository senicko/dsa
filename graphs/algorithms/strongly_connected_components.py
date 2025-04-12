from math import inf
from queue import PriorityQueue


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


def compute_finish_times(graph):
    n = len(graph)
    time = 0
    visited = [False] * n
    finish = [inf] * n

    def dfs_visit(v):
        nonlocal time
        time += 1

        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                dfs_visit(u)

        time += 1
        finish[v] = time

    for v in range(n):
        if not visited[v]:
            visited[v] = True
            dfs_visit(v)

    return finish


def extract_components(graph, visit_times):
    n = len(graph)
    components = []
    visited = [False] * n
    priority_queue = PriorityQueue()

    for v in range(n):
        # Lower number has a higher priority, so we insert
        # vertices with negative visit times.
        priority_queue.put(PriorityQueueEntry(-visit_times[v], v))

    def dfs_visit(v):
        for u in graph[v]:
            if not visited[u]:
                components[-1].append(u)
                visited[u] = True
                dfs_visit(u)

    # Process vertices in descending order of
    # their discovery times.

    while not priority_queue.empty():
        v = priority_queue.get().value

        if not visited[v]:
            components.append([v])
            visited[v] = True
            dfs_visit(v)

    return components


def strongly_connected_components(graph):
    finish_times = compute_finish_times(graph)
    transpose = build_transpose(graph)
    return extract_components(transpose, finish_times)


if __name__ == "__main__":
    graph = [[1], [2, 6, 5], [3], [4, 2], [4], [0, 2], [3, 7], [4, 6]]
    print(strongly_connected_components(graph))
