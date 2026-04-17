"""
Recursion on Data Structures: Binary Tree
==========================================
Trees are the most natural recursive structure. Every tree operation
follows the same pattern:
    1. Base case: if not root → return default
    2. Process root
    3. Recurse on root.left and root.right
    4. Combine results
"""

from collections import deque


class TreeNode:
    """Binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ── Helper: build tree from level-order list ──────────────────
def build_tree(values: list) -> TreeNode:
    """Build a tree from a list like [1, 2, 3, None, 4, 5]."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ── 1. Tree Traversals ───────────────────────────────────────
def inorder(root: TreeNode) -> list:
    """Left → Root → Right. For BST, this gives sorted order."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def preorder(root: TreeNode) -> list:
    """Root → Left → Right. Useful for serialization."""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def postorder(root: TreeNode) -> list:
    """Left → Right → Root. Useful for deletion and evaluation."""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# ── 2. Max Depth ─────────────────────────────────────────────
def max_depth(root: TreeNode) -> int:
    """Height of the tree. Classic divide-and-conquer on trees."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ── 3. Invert (Mirror) a Binary Tree ────────────────────────
def invert_tree(root: TreeNode) -> TreeNode:
    """Swap left and right children at every level."""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# ── 4. Check if Symmetric ───────────────────────────────────
def is_symmetric(root: TreeNode) -> bool:
    """A tree is symmetric if its left and right subtrees mirror each other."""
    def mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val
                and mirror(t1.left, t2.right)
                and mirror(t1.right, t2.left))
    return mirror(root, root) if root else True


# ── 5. Path Sum ──────────────────────────────────────────────
def has_path_sum(root: TreeNode, target: int) -> bool:
    """Check if any root-to-leaf path sums to target."""
    if not root:
        return False
    # Leaf node: check if remaining target matches
    if not root.left and not root.right:
        return root.val == target
    # Recurse: subtract current value and check both subtrees
    remainder = target - root.val
    return has_path_sum(root.left, remainder) or has_path_sum(root.right, remainder)


# ── 6. Lowest Common Ancestor ───────────────────────────────
def lca(root: TreeNode, p: int, q: int) -> TreeNode:
    """Find LCA of nodes with values p and q."""
    if not root or root.val == p or root.val == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root       # p and q are in different subtrees
    return left or right   # both are in the same subtree


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    tree = build_tree([1, 2, 3, 4, 5, None, 6])

    print("Tree: [1, 2, 3, 4, 5, None, 6]")
    print(f"Inorder:    {inorder(tree)}")
    print(f"Preorder:   {preorder(tree)}")
    print(f"Postorder:  {postorder(tree)}")
    print(f"Max depth:  {max_depth(tree)}")

    # Symmetric tree test
    sym_tree = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(f"\nSymmetric tree [1,2,2,3,4,4,3]: {is_symmetric(sym_tree)}")
    print(f"Original tree symmetric: {is_symmetric(tree)}")

    # Path sum
    print(f"\nHas path sum 7 (1→2→4): {has_path_sum(tree, 7)}")
    print(f"Has path sum 9 (1→2→5+1=8, no): {has_path_sum(tree, 9)}")

    # LCA
    ancestor = lca(tree, 4, 5)
    print(f"\nLCA of 4 and 5: {ancestor.val}")
    ancestor = lca(tree, 4, 6)
    print(f"LCA of 4 and 6: {ancestor.val}")
