"""
Implementacja BST oparta na Cormen'ie
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Visits nodes in order.
    def inorder_walk(self):
        self._inorder_walk(self.root)

    def _inorder_walk(self, node):
        if node is not None:
            self._inorder_walk(node.left)
            print(node.value)
            self._inorder_walk(node.right)

    # Inserts the value to the BST.
    # Runs in O(h) time.
    def insert(self, value):
        # Store pointers to current node we'll compare to
        # and current parent of inserted value.
        cmp = self.root
        parent = None

        # While there is a node we can compare to
        while cmp:
            # Set it to parent.
            parent = cmp

            # Float down the tree according to
            # standard BST property.
            if value < cmp.value:
                # This new cmp potentially is our new parent
                # in the next iteration.
                cmp = cmp.left
            else:
                cmp = cmp.right

        # Create new node and assign found parent.
        new = Node(value)
        new.parent = parent

        # If the parent is None, we are the first node in the tree (root)
        # Otherwise, attach to left or right leaf of parent.

        # Notice that the wile above guarantees that the side we'll
        # choose must be empty.

        if parent is None:
            self.root = new
        elif value < parent.value:
            parent.left = new
        else:
            parent.right = new

    # Search for value recursively.
    # Runs in O(h) time.
    def search(self, value):
        self._search(self.root, value)

    def _search(self, current, value):
        if current is None or current.value == value:
            return current

        if value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    # Search for value iteratively
    # Runs in O(h) time.
    def search_iter(self, value):
        current = self.root

        while current and current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return current

    # Find min from the given root.
    # Runs in O(h) time.
    def min(self, root=None):
        curr = root if root else self.root

        while curr.left:
            curr = curr.left

        return curr

    # Find max node from the given root.
    # Runs in O(h) time.
    def max(self, root=None):
        curr = root if root else self.root

        while curr.right:
            curr = curr.right

        return curr

    # Find next node in in-order walk order.
    # Runs in O(h) time.
    def successor(self, node):
        # If node has right child, find min in right subtree.
        if node.right:
            return self.min(node.right)

        # Otherwise find first parent in whose left subtree we are.
        parent = node.parent

        # While parent exists and current node is it's right child
        # (so parent isn't next in in-order walk)
        while parent is not None and node is parent.right:
            node = parent
            parent = parent.parent

        return parent

    # Transplant replaces subtree rooted at u with subtree rooted at v.
    # Visually detach the subtree u, and replace it with v.
    # This operation is just a util and DOES NOT maintain BST property.
    def transplant(self, u, v):
        if u is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.p = u.p

    def remove(self, x):
        if x.left is None:
            self.transplant(x, x.right)
            return

        if x.right is None:
            self.transplant(x, x.left)
            return

        y = self.min(x.right)

        if y is not x.right:
            self.transplant(y, y.right)
            y.right = x
            y.right.p = y

        self.transplant(x, y)
        y.left = x.left
        y.left.parent = y
