"""
Trees in DSA — 5. AVL Tree (Self-Balancing BST)
Guarantees O(log n) by keeping |height(left) - height(right)| ≤ 1.
Uses rotations to rebalance after insert/delete.

4 rotation cases (examples use concrete values — see rotate_right /
rotate_left docstrings for detailed tree diagrams):
  LL → single right rotation
       e.g. {30, 20, 10} inserted in left-of-left → right-rotate(30)
  RR → single left rotation
       e.g. {10, 20, 30} inserted in right-of-right → left-rotate(10)
  LR → left rotate child, then right rotate root
       e.g. {30, 10, 20} → left-rotate(10); right-rotate(30) → 20 on top
  RL → right rotate child, then left rotate root
       e.g. {10, 30, 20} → right-rotate(30); left-rotate(10) → 20 on top
"""


class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# ---- Height & Balance helpers ----

def get_height(node):
    return node.height if node else 0


def get_balance(node):
    """Positive = left-heavy, Negative = right-heavy."""
    return get_height(node.left) - get_height(node.right) if node else 0


def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))


# ---- Rotations ----

def rotate_right(z):
    r"""
    Right rotation (fixes LL imbalance).

    Example — right-rotate at 30:

         30                        20
        /  \                      /  \
       20   40                  10    30
      /  \         ───►        / \    / \
     10   25                  5  15  25  40
     / \
    5   15

    The middle node (20) rises; 30's old left subtree (25) becomes
    20's new right child's left subtree.
    """
    y = z.left
    t3 = y.right

    y.right = z
    z.left = t3

    update_height(z)
    update_height(y)
    return y


def rotate_left(z):
    r"""
    Left rotation (fixes RR imbalance).

    Example — left-rotate at 20:

        20                              50
       /  \                            /  \
      10   50                        20    60
           / \         ───►         / \    / \
          30  60                   10 30  55  70
              / \
            55   70

    The middle node (50) rises; 20's old right subtree (30) becomes
    20's new right child.
    """
    y = z.right
    t2 = y.left

    y.left = z
    z.right = t2

    update_height(z)
    update_height(y)
    return y


# ---- Insert ----

def avl_insert(node, val):
    """Insert a value and rebalance if needed."""

    # 1. Standard BST insert
    if not node:
        return AVLNode(val)
    if val < node.val:
        node.left = avl_insert(node.left, val)
    elif val > node.val:
        node.right = avl_insert(node.right, val)
    else:
        return node  # duplicates ignored

    # 2. Update height
    update_height(node)

    # 3. Check balance and rotate
    balance = get_balance(node)

    # LL case: left-heavy AND inserted in left-of-left
    if balance > 1 and val < node.left.val:
        return rotate_right(node)

    # RR case: right-heavy AND inserted in right-of-right
    if balance < -1 and val > node.right.val:
        return rotate_left(node)

    # LR case: left-heavy AND inserted in right-of-left
    if balance > 1 and val > node.left.val:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    # RL case: right-heavy AND inserted in left-of-right
    if balance < -1 and val < node.right.val:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node


# ---- Delete ----

def avl_delete(node, val):
    """Delete a value and rebalance."""

    if not node:
        return None

    # 1. Standard BST delete
    if val < node.val:
        node.left = avl_delete(node.left, val)
    elif val > node.val:
        node.right = avl_delete(node.right, val)
    else:
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        # Two children: replace with inorder successor
        succ = node.right
        while succ.left:
            succ = succ.left
        node.val = succ.val
        node.right = avl_delete(node.right, succ.val)

    # 2. Update height
    update_height(node)

    # 3. Rebalance (same logic, but check child balance for LR/RL)
    balance = get_balance(node)

    if balance > 1 and get_balance(node.left) >= 0:
        return rotate_right(node)

    if balance > 1 and get_balance(node.left) < 0:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    if balance < -1 and get_balance(node.right) <= 0:
        return rotate_left(node)

    if balance < -1 and get_balance(node.right) > 0:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node


# ---- Utility ----

def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def print_tree(node, level=0, prefix="Root: "):
    """Pretty-print the tree structure."""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val)
              + f" (h={node.height}, bal={get_balance(node)})")
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")


# --- Demo ---
if __name__ == "__main__":
    root = None

    # Inserting sorted values — would break a normal BST,
    # but AVL stays balanced via rotations
    print("Inserting: 1, 2, 3, 4, 5, 6, 7")
    for v in [1, 2, 3, 4, 5, 6, 7]:
        root = avl_insert(root, v)

    print(f"\nInorder: {inorder(root)}")
    print(f"Tree height: {get_height(root)} (log2(7) ≈ 2.8 → stays balanced!)")
    print("\nTree structure:")
    print_tree(root)

    print("\nDeleting 4...")
    root = avl_delete(root, 4)
    print(f"Inorder: {inorder(root)}")
    print_tree(root)
