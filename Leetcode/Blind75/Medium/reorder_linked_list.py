# Problem : https://leetcode.com/problems/reorder-list/description/?envType=problem-list-v2&envId=oizxjoit

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # --- Step 1: Find the middle using slow/fast pointers ---
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next        # moves 1 step
            fast = fast.next.next   # moves 2 steps — when fast hits end, slow is at middle

        # --- Step 2: Split into two halves ---
        prev, curr = None, slow.next  # second half starts just after slow
        slow.next = None              # sever the first half here

        # --- Step 3: Reverse the second half ---
        while curr:
            next_temp = curr.next  # save next before overwriting
            curr.next = prev       # flip the pointer backward
            prev = curr            # prev advances to current node
            curr = next_temp       # move forward
        # prev is now the head of the reversed second half

        # --- Step 4: Interleave the two halves ---
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next  # save both next pointers
            first.next = second                    # first half node -> second half node
            second.next = tmp1                     # second half node -> next of first half
            first, second = tmp1, tmp2             # advance both pointers


if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Reorder the list
    Solution().reorderList(head)
    
    # Print the reordered list
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next



# Strategy to solve the problem:
# 1. Use the slow and fast pointer technique to find the middle of the linked list
# 2. Reverse the second half of the linked list
# 3. Merge the two halves of the linked list by alternating nodes from each half
