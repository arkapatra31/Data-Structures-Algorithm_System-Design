"""
Trees in DSA — 4. Common Patterns
These patterns cover ~80% of tree interview questions.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ============================================================
#  PATTERN 1: Height / Depth
# ============================================================

def height(node):
    """Height of tree = longest root-to-leaf path."""
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def min_depth(node):
    """Shortest root-to-leaf path."""
    if not node:
        return 0
    if not node.left:
        return 1 + min_depth(node.right)
    if not node.right:
        return 1 + min_depth(node.left)
    return 1 + min(min_depth(node.left), min_depth(node.right))


# ============================================================
#  PATTERN 2: Balanced Check
# ============================================================

def is_balanced(node):
    """A tree is balanced if height diff ≤ 1 at every node."""
    if not node:
        return True
    lh, rh = height(node.left), height(node.right)
    return (abs(lh - rh) <= 1
            and is_balanced(node.left)
            and is_balanced(node.right))


def is_balanced_optimal(node):
    """O(n) version — check balance during height computation."""
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(node) != -1


# ============================================================
#  PATTERN 3: Lowest Common Ancestor (LCA)
# ============================================================

def lca_bst(root, p, q):
    """LCA in a BST — use BST property for O(log n)."""
    while root:
        if p < root.val and q < root.val:
            root = root.left
        elif p > root.val and q > root.val:
            root = root.right
        else:
            return root.val  # split point = LCA


def lca_binary_tree(root, p, q):
    """LCA in a general binary tree — O(n)."""
    if not root or root.val == p or root.val == q:
        return root
    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)
    if left and right:
        return root  # p and q are in different subtrees
    return left or right


# ============================================================
#  PATTERN 4: Validate BST
# ============================================================

def is_valid_bst(node, low=float('-inf'), high=float('inf')):
    """Check BST property: low < node.val < high at every node."""
    if not node:
        return True
    if not (low < node.val < high):
        return False
    return (is_valid_bst(node.left, low, node.val)
            and is_valid_bst(node.right, node.val, high))


# ============================================================
#  PATTERN 5: Path Sum
# ============================================================

def has_path_sum(node, target):
    """Does any root-to-leaf path sum to target?"""
    if not node:
        return False
    if not node.left and not node.right:  # leaf
        return node.val == target
    return (has_path_sum(node.left, target - node.val)
            or has_path_sum(node.right, target - node.val))


def all_path_sums(node, target):
    """Return ALL root-to-leaf paths that sum to target."""
    result = []

    def dfs(node, remaining, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and remaining == node.val:
            result.append(list(path))
        dfs(node.left, remaining - node.val, path)
        dfs(node.right, remaining - node.val, path)
        path.pop()

    dfs(node, target, [])
    return result


# ============================================================
#  PATTERN 6: Diameter
# ============================================================

def diameter(root):
    """Longest path between any two nodes (may not pass through root)."""
    best = [0]

    def dfs(node):
        if not node:
            return 0
        l, r = dfs(node.left), dfs(node.right)
        best[0] = max(best[0], l + r)  # path through this node
        return 1 + max(l, r)           # return height

    dfs(root)
    return best[0]


# ============================================================
#  PATTERN 7: Serialize / Deserialize
# ============================================================

def serialize(root):
    """Preorder serialization — 'N' for null nodes."""
    if not root:
        return "N"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"


def deserialize(data):
    """Reconstruct tree from preorder serialization."""
    vals = iter(data.split(","))

    def build():
        v = next(vals)
        if v == "N":
            return None
        node = TreeNode(int(v))
        node.left = build()
        node.right = build()
        return node

    return build()


# ============================================================
#  PATTERN 8: Invert / Mirror
# ============================================================

def invert_tree(node):
    """Swap left and right children at every node."""
    if not node:
        return None
    node.left, node.right = invert_tree(node.right), invert_tree(node.left)
    return node


def is_symmetric(root):
    """Check if tree is a mirror of itself."""
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return (a.val == b.val
                and mirror(a.left, b.right)
                and mirror(a.right, b.left))

    return mirror(root, root) if root else True


# ============================================================
#  PATTERN 9: Views (Right side view)
# ============================================================

def right_side_view(root):
    """What you see looking at the tree from the right."""
    from collections import deque
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)  # last node at each level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


# --- Demo ---
if __name__ == "__main__":
    # Build:    10
    #          /  \
    #         5    15
    #        / \     \
    #       3   7    20
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)

    print(f"Height:      {height(root)}")
    print(f"Balanced:    {is_balanced(root)}")
    print(f"Valid BST:   {is_valid_bst(root)}")
    print(f"LCA(3,7):    {lca_bst(root, 3, 7)}")
    print(f"PathSum(18): {has_path_sum(root, 18)}")
    print(f"Diameter:    {diameter(root)}")
    print(f"Right view:  {right_side_view(root)}")

    s = serialize(root)
    print(f"Serialized:  {s}")
    root2 = deserialize(s)
    print(f"Re-serial:   {serialize(root2)}")
