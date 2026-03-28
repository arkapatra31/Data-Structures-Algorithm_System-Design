from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, digit = divmod(val, 10)
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next
    
if __name__ == "__main__":
    # l1 = [0,1] l2 = [4,4,5]
    l1 = ListNode(0)
    l1.next = ListNode(1)

    l2 = ListNode(4)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)

    sum_list = Solution().addTwoNumbers(l1, l2)
    while sum_list:
        print(sum_list.val, end="-> ")
        sum_list = sum_list.next
    print("None")