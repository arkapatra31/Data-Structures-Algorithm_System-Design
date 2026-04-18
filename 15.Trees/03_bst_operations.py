"""
Trees in DSA — 3. Binary Search Tree (BST)
Insert, search, delete, min, max, and inorder successor.

BST property: left < node < right at every node.
Average O(log n) — worst O(n) when tree is skewed.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ---- Insert ----
    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node  # duplicates ignored

    # ---- Search ----
    def search(self, val):
        """Iterative search — O(log n) average."""
        node = self.root
        while node:
            if val == node.val:
                return True
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return False

    # ---- Delete ----
    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Case 1 & 2: zero or one child
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Case 3: two children
            # Replace with inorder successor (smallest in right subtree)
            successor = self._find_min_node(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)

        return node

    # ---- Min / Max ----
    def find_min(self):
        """Leftmost node = minimum."""
        node = self._find_min_node(self.root)
        return node.val if node else None

    def _find_min_node(self, node):
        while node and node.left:
            node = node.left
        return node

    def find_max(self):
        """Rightmost node = maximum."""
        node = self.root
        while node and node.right:
            node = node.right
        return node.val if node else None

    # ---- Inorder successor ----
    def inorder_successor(self, val):
        """
        Find the node with the smallest value greater than val.
        Used in delete and iterator problems.
        """
        successor = None
        node = self.root
        while node:
            if val < node.val:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor.val if successor else None

    # ---- Utility: inorder traversal ----
    def inorder(self):
        """Returns sorted list of all values."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)


# --- Demo ---
if __name__ == "__main__":
    bst = BST()
    for val in [10, 5, 15, 3, 7, 12, 20]:
        bst.insert(val)

    print(f"Inorder (sorted): {bst.inorder()}")
    print(f"Search 7:  {bst.search(7)}")
    print(f"Search 8:  {bst.search(8)}")
    print(f"Min: {bst.find_min()}, Max: {bst.find_max()}")
    print(f"Successor of 7: {bst.inorder_successor(7)}")

    bst.delete(5)
    print(f"After deleting 5: {bst.inorder()}")
