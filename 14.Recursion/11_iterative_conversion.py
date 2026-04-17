"""
Converting Recursion to Iteration
===================================
Python has a ~1000 recursion limit. For deep recursion,
convert to iteration using an explicit stack.

This file shows the recursive version side-by-side with
the iterative equivalent for common tree operations.
"""

import sys
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list) -> TreeNode:
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


# ══════════════════════════════════════════════════════════════
# 1. INORDER TRAVERSAL
# ══════════════════════════════════════════════════════════════

def inorder_recursive(root: TreeNode) -> list:
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def inorder_iterative(root: TreeNode) -> list:
    """
    Uses an explicit stack to simulate the call stack.
    Pattern: go as far left as possible, process, then go right.
    """
    result = []
    stack = []
    curr = root

    while curr or stack:
        # Push all left children
        while curr:
            stack.append(curr)
            curr = curr.left

        # Process current node
        curr = stack.pop()
        result.append(curr.val)

        # Move to right subtree
        curr = curr.right

    return result


# ══════════════════════════════════════════════════════════════
# 2. PREORDER TRAVERSAL
# ══════════════════════════════════════════════════════════════

def preorder_recursive(root: TreeNode) -> list:
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def preorder_iterative(root: TreeNode) -> list:
    """Stack-based: process node, push right then left (LIFO reversal)."""
    if not root:
        return []
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push right first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# ══════════════════════════════════════════════════════════════
# 3. MAX DEPTH
# ══════════════════════════════════════════════════════════════

def max_depth_recursive(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth_recursive(root.left), max_depth_recursive(root.right))


def max_depth_iterative(root: TreeNode) -> int:
    """BFS approach: count levels."""
    if not root:
        return 0
    depth = 0
    queue = deque([root])

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


# ══════════════════════════════════════════════════════════════
# 4. FACTORIAL (simple linear recursion → loop)
# ══════════════════════════════════════════════════════════════

def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Linear recursion always converts to a simple loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ══════════════════════════════════════════════════════════════
# 5. DFS ON GRAPH (recursive → iterative)
# ══════════════════════════════════════════════════════════════

def dfs_recursive(graph: dict, start: str, visited: set = None) -> list:
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    return result


def dfs_iterative(graph: dict, start: str) -> list:
    """Replace call stack with explicit stack."""
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        # Add neighbors in reverse for consistent ordering
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return result


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Python recursion limit: {sys.getrecursionlimit()}")

    tree = build_tree([1, 2, 3, 4, 5, 6, 7])

    print("\n=== Inorder ===")
    print(f"  Recursive: {inorder_recursive(tree)}")
    print(f"  Iterative: {inorder_iterative(tree)}")

    print("\n=== Preorder ===")
    print(f"  Recursive: {preorder_recursive(tree)}")
    print(f"  Iterative: {preorder_iterative(tree)}")

    print("\n=== Max Depth ===")
    print(f"  Recursive: {max_depth_recursive(tree)}")
    print(f"  Iterative: {max_depth_iterative(tree)}")

    print("\n=== Factorial(10) ===")
    print(f"  Recursive: {factorial_recursive(10)}")
    print(f"  Iterative: {factorial_iterative(10)}")

    print("\n=== Graph DFS ===")
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    print(f"  Graph: {graph}")
    print(f"  Recursive DFS: {dfs_recursive(graph, 'A')}")
    print(f"  Iterative DFS: {dfs_iterative(graph, 'A')}")
