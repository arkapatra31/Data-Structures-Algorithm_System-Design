from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head      # Tortoise - moves 1 step
        fast = head      # Hare - moves 2 steps
        
        while fast and fast.next:
            print(f"Slow: {slow.val}, Fast: {fast.val}")
            slow = slow.next
            fast = fast.next.next
            print(f"Slow: {slow.val}, Fast: {fast.val}")
            print("-"*20)
            if slow == fast:  # Pointers meet = cycle found
                print("Cycle found")
                print(f"Slow: {slow.val}, Fast: {fast.val}")
                print("-"*20)
                return True
        
        return False 


if __name__ == "__main__":
    # 3 2 0 -4 10
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = ListNode(10)
    head.next.next.next.next.next = head.next
    print(Solution().hasCycle(head))