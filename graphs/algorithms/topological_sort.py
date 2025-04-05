class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print(self, map):
        repr = ""
        curr = self
        count = 0

        while curr:
            repr += f"{count}. {map[curr.value]}\n"
            curr = curr.next
            count += 1

        print(repr)


def topological_sort(graph):
    n = len(graph)
    sorted = None
    visited = [False] * n

    def dfs_visit(v):
        nonlocal sorted
        visited[v] = True

        for u in graph[v]:
            if not visited[u]:
                dfs_visit(u)

        node = Node(v)
        node.next = sorted
        sorted = node

    # Run DFS visit for every node so that
    # we don't skip disconnected components.
    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return sorted


if __name__ == "__main__":
    names = {
        0: "undershorts",
        1: "pants",
        2: "belt",
        3: "shirt",
        4: "tie",
        5: "jacket",
        6: "shoes",
        7: "socks",
        8: "watch"
    }

    graph = [
        [1, 6],  # undershorts
        [2, 6],  # pants
        [5],  # belt
        [2, 4],  # shirt
        [5],  # tie
        [],  # jacket
        [],  # shoes
        [6],  # socks
        []  # watch
    ]

    sorted_events = topological_sort(graph)
    sorted_events.print(names)
