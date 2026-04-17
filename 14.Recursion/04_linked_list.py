"""
Recursion on Data Structures: Linked List
==========================================
Linked lists are inherently recursive: a list is either empty (None)
or a node followed by a smaller list (node.next).

All operations demonstrated recursively with helper utilities.
"""


class ListNode:
    """Singly linked list node."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        node = self
        while node:
            vals.append(str(node.val))
            node = node.next
        return " → ".join(vals)


# ── Helper: build a list from Python list ─────────────────────
def build_list(values: list) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    head.next = build_list(values[1:])
    return head


# ── 1. Reverse a Linked List ─────────────────────────────────
def reverse(head: ListNode) -> ListNode:
    """
    Reverse the list recursively.
    Key insight: reverse the rest, then make the next node point back.
    """
    # Base case: empty or single node
    if not head or not head.next:
        return head

    new_head = reverse(head.next)  # reverse everything after me
    head.next.next = head          # make next node point back to me
    head.next = None               # break my forward pointer
    return new_head


# ── 2. Search for a Value ────────────────────────────────────
def search(head: ListNode, target: int) -> bool:
    """Check if target exists in the list."""
    if not head:
        return False
    if head.val == target:
        return True
    return search(head.next, target)


# ── 3. Get Length ─────────────────────────────────────────────
def length(head: ListNode) -> int:
    """Count nodes recursively."""
    if not head:
        return 0
    return 1 + length(head.next)


# ── 4. Remove All Occurrences of a Value ─────────────────────
def remove_value(head: ListNode, target: int) -> ListNode:
    """Remove every node with val == target."""
    if not head:
        return None
    head.next = remove_value(head.next, target)  # clean the rest first
    if head.val == target:
        return head.next  # skip this node
    return head


# ── 5. Merge Two Sorted Lists ────────────────────────────────
def merge_sorted(l1: ListNode, l2: ListNode) -> ListNode:
    """Merge two sorted lists into one sorted list."""
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val <= l2.val:
        l1.next = merge_sorted(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted(l1, l2.next)
        return l2


# ── Demo ──────────────────────────────────────────────────────
if __name__ == "__main__":
    # Build and display
    lst = build_list([1, 2, 3, 4, 5])
    print(f"Original:    {lst}")
    print(f"Length:      {length(lst)}")
    print(f"Search(3):   {search(lst, 3)}")
    print(f"Search(9):   {search(lst, 9)}")

    # Reverse
    reversed_lst = reverse(lst)
    print(f"Reversed:    {reversed_lst}")

    # Remove value
    lst2 = build_list([1, 3, 2, 3, 4, 3, 5])
    print(f"\nBefore remove(3): {lst2}")
    lst2 = remove_value(lst2, 3)
    print(f"After remove(3):  {lst2}")

    # Merge sorted
    a = build_list([1, 3, 5, 7])
    b = build_list([2, 4, 6, 8])
    print(f"\nMerge {a}")
    print(f"  and {b}")
    print(f"  →   {merge_sorted(a, b)}")
