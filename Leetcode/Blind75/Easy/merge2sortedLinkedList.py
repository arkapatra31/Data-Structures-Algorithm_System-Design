from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Compare and merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes from the non-empty list
        if list1:
            current.next = list1
        else:
            current.next = list2
            
        return dummy.next




def print_list(head):
    """Helper function to print linked list"""
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    return " -> ".join(result) + " -> None" if result else "Empty"

if __name__ == "__main__":
    # Test Case 1: [1,2,4] and [1,3,4] -> [1,1,2,3,4,4]
    print("Test Case 1:")
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    print(f"List1: {print_list(list1)}")
    
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    print(f"List2: {print_list(list2)}")
    
    result1 = Solution().mergeTwoLists(list1, list2)
    print(f"Merged: {print_list(result1)}")
    
    # Test Case 2: [] and [] -> []
    print("\nTest Case 2:")
    result2 = Solution().mergeTwoLists(None, None)
    print(f"Merged empty lists: {print_list(result2)}")
    
    # Test Case 3: [] and [0] -> [0]
    print("\nTest Case 3:")
    list3 = ListNode(0)
    result3 = Solution().mergeTwoLists(None, list3)
    print(f"Merged empty and [0]: {print_list(result3)}")