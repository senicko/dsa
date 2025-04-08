from math import inf
from queue import PriorityQueue


class PriorityQueueEntry(object):
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        return self.priority < other.priority


# Reverses the direction of edges in the graph.
def build_transpose(graph):
    n = len(graph)
    transpose = [[] for _ in range(n)]

    for v in range(n):
        for neighbour in graph[v]:
            transpose[neighbour].append(v)

    return transpose


# Builds a transpose of the given graph.
def transpose_dfs(graph, visit_times):
    n = len(graph)

    forests = []
    visited = [False] * n

    def dfs_visit(v):
        for u in graph[v]:
            if not visited[u]:
                forests[-1].append(u)
                visited[u] = True
                dfs_visit(u)

    # Process vertices in order of their finish times.

    priority_queue = PriorityQueue()

    for v in range(n):
        priority_queue.put(PriorityQueueEntry(-visit_times[v], v))

    while not priority_queue.empty():
        entry = priority_queue.get()
        v = entry.data

        if not visited[v]:
            forests.append([v])
            visited[v] = True
            dfs_visit(v)

    return forests


# Computes BFS finish times for every node.
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


def strongly_connected_components(graph):
    finish_times = compute_finish_times(graph)
    transpose = build_transpose(graph)
    return transpose_dfs(transpose, finish_times)


if __name__ == "__main__":
    graph = [[1], [2, 6, 5], [3], [4, 2], [4], [0, 2], [3, 7], [4, 6]]
    print(strongly_connected_components(graph))
