class Node:
    def __init__(self, v):
        self.v = v
        self.parent = self
        self.rank = 0


def find(x):
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x

        if x.rank == y.rank:
            x.rank += 1


def extract_edges(G):
    n = len(G)
    edges = []
    total_weight = 0

    for u in range(n):
        for v, w in G[u]:
            if v > u:
                total_weight += w
                edges.append((w, u, v))

    return edges, total_weight


def lufthansa(G):
    n = len(G)

    edges, total_weight = extract_edges(G)
    edges.sort(reverse=True)

    sets = [Node(v) for v in range(n)]

    mst_weight = 0
    has_exception = False

    for w, u, v in edges:
        u_set = sets[u]
        v_set = sets[v]

        if find(u_set) != find(v_set):
            union(u_set, v_set)
            mst_weight += w
        elif not has_exception:
            has_exception = True
            mst_weight += w

    return total_weight - mst_weight
