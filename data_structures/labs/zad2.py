# Proszę zaimplementować następujące operacje na drzewie BST
#
# 1) Wstawianie do drzewa BST
# 2) następnik / poprzednik
# 3) znalezienie minimum

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        cmp = self.root
        parent = None

        while cmp:
            parent = cmp

            if value < cmp.value:
                cmp = cmp.left
            else:
                cmp = cmp.right

        new = Node(value)
        new.parent = parent

        if parent is None:
            self.root = new
        elif value < parent.value:
            parent.left = new
        else:
            parent.right = new

    def min(self, root=None):
        curr = root if root is not None else None

        while curr.left:
            curr = curr.left

        return curr

    def successor(self, node):
        if node.right:
            return self.min(node.right)

        parent = node.parent

        while parent is not None and node is parent.right:
            node = parent
            parent = node.parent

        return parent
