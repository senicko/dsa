"""
Disjoint set with Path Compression and Rank heuristics.

Rank Heuristic:
    When we union two sets (represented as trees) we
    attach smaller tree to the root of the taller tree.
    This makes our trees shorter, and improves efficiency of find(x).

Path Compression:
    find(x) returns the root of the x's set.
    During find operation, we set x's parent to the root of its set.
    Thanks to this, we don't have to traverse all the intermediate
    nodes again in another call to find(x).
"""


class Node:
    def __init__(self):
        self.x = None
        self.parent = None
        self.rank = None


# Creates a new root node of a tree set.
def make_set(x):
    root = Node()
    root.x = x
    root.parent = root
    root.rank = 0
    return root


# Union joins two sets using rank heuristic.
def union(x, y):
    # Replace x and y with root's
    # of their sets.
    x = find(x)
    y = find(y)

    # If both x and y belong to the
    # same set, do nothing.
    if x == y:
        return

    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        # If both sets had the same rank, increment
        # the height estimate.
        if x.rank == y.rank:
            y.rank = y.rank + 1


# Follows the path to the root of
# the current set.
def find(x):
    # If x is not the root of the set
    # apply path compression.
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent
