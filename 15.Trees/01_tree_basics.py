"""
Trees in DSA — 1. Basics
TreeNode class and tree construction
"""


class TreeNode:
    """Binary tree node — the foundation for everything."""

    def __init__(self, val):
        self.val = val
        self.left = None  # left child
        self.right = None  # right child

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_sample_tree():
    """
    Builds this tree:
            10
           /  \\
          5    15
         / \\     \\
        3   7    20
       /
      1
    """
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    root.left.left.left = TreeNode(1)
    return root


def count_nodes(node):
    """Count total nodes in tree."""
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def is_leaf(node):
    """Check if a node is a leaf (no children)."""
    return node is not None and not node.left and not node.right


def get_leaves(node):
    """Return all leaf values."""
    if not node:
        return []
    if is_leaf(node):
        return [node.val]
    return get_leaves(node.left) + get_leaves(node.right)


# --- Demo ---
if __name__ == "__main__":
    root = build_sample_tree()
    print(f"Root:        {root.val}")
    print(f"Total nodes: {count_nodes(root)}")
    print(f"Leaves:      {get_leaves(root)}")
