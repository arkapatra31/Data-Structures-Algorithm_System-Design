from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4
        # 4 -> 3 -> 2 -> 1 -> None
        prev = None
        current = head
        while current:
            next = current.next # Preserve the next in variable : 2, 3
            current.next = prev # Break the link and set to prev 2->1 ->None
            prev = current # Move the prev pointer to curent prev = 2->1->None
            current = next # Move the current pointer to next current = 3

        return prev

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseList(head))