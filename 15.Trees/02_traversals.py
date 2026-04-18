"""
Trees in DSA — 2. Traversals
Inorder, Preorder, Postorder (DFS) and Level Order (BFS)
Both recursive and iterative versions.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_sample_tree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    root.left.left.left = TreeNode(1)
    return root


# ============================================================
#  RECURSIVE VERSIONS
# ============================================================

def inorder(node):
    """Left → Root → Right  (gives sorted order in BST)"""
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def preorder(node):
    """Root → Left → Right  (used to copy / serialize a tree)"""
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)


def postorder(node):
    """Left → Right → Root  (used to delete a tree bottom-up)"""
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]


def level_order(root):
    """Level by level, left to right  (BFS — uses a queue)"""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# ============================================================
#  ITERATIVE VERSIONS (important for interviews)
# ============================================================

def inorder_iterative(root):
    """Iterative inorder using an explicit stack."""
    result, stack, curr = [], [], root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result


def preorder_iterative(root):
    """Iterative preorder using a stack."""
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)  # right first so left is processed first
        if node.left:
            stack.append(node.left)
    return result


def postorder_iterative(root):
    """Iterative postorder using two stacks."""
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]  # reverse at the end


def level_order_grouped(root):
    """Level order but grouped by level — returns list of lists."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


# --- Demo ---
if __name__ == "__main__":
    root = build_sample_tree()

    print("=== Recursive ===")
    print(f"Inorder:     {inorder(root)}")
    print(f"Preorder:    {preorder(root)}")
    print(f"Postorder:   {postorder(root)}")
    print(f"Level order: {level_order(root)}")

    print("\n=== Iterative ===")
    print(f"Inorder:     {inorder_iterative(root)}")
    print(f"Preorder:    {preorder_iterative(root)}")
    print(f"Postorder:   {postorder_iterative(root)}")

    print(f"\nGrouped:     {level_order_grouped(root)}")
