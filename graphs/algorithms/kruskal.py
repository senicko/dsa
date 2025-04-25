class Node:
    def __init__(self, v):
        self.parent = None
        self.v = v
        self.rank = 0


def make_set(v):
    root = Node(v)
    root.parent = root
    return root


def find(v):
    if v is not v.parent:
        v.parent = find(v.parent)
    return v.parent


def union(u, v):
    u = find(u)
    v = find(v)

    if u == v:
        return

    if u.rank < v.rank:
        u.parent = v
    else:
        v.parent = u

        if v.rank == u.rank:
            u.rank += 1


def kruskal(graph):
    n = len(graph)
    mst = []

    # Create a list of the edges in graph.

    edges = []

    for u in range(n):
        for v, w in graph[u]:
            edges.append((u, v, w))

    # Sort edges in ascending order.

    edges.sort(key=lambda x: x[2])

    # Create a set from every vertex.

    sets = [None] * n

    for u in range(n):
        sets[u] = make_set(u)

    # Process edges in ascending order
    # of weights.

    for e in edges:
        u, v, _ = e
        u = sets[u]
        v = sets[v]

        if find(u) is not find(v):
            mst.append(e)
            union(u, v)

    return mst


if __name__ == "__main__":
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    graph = [
        [(1, 4), (7, 8)],  # 0: a
        [(0, 4), (2, 8), (7, 11)],  # 1: b
        [(1, 8), (3, 7), (5, 4), (8, 2)],  # 2: c
        [(2, 7), (4, 9), (5, 14)],  # 3: d
        [(3, 9), (5, 10)],  # 4: e
        [(2, 4), (3, 14), (4, 10), (6, 2)],  # 5: f
        [(5, 2), (7, 1), (8, 6)],  # 6: g
        [(0, 8), (1, 11), (6, 1), (8, 7)],  # 7: h
        [(2, 2), (6, 6), (7, 7)]  # 8: i
    ]

    mst = kruskal(graph)

    print("Found MST: ")
    for u, v, w in mst:
        print(f"{nodes[u]} -({w})- {nodes[v]}")
