class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def swapPairs(self, head: Node) -> Node:
        # 1 -> 2 -> 3 -> 4 -> 5
        # 2 -> 1 -> 4 -> 3 -> 5
        # dummy = Node(0)
        # dummy.next = head
        # prev = dummy

        # while prev.next and prev.next.next:
        #     a = prev.next        # first node of pair
        #     b = prev.next.next   # second node of pair

        #     prev.next = b        # connect prev to second node
        #     a.next = b.next      # first node skips past second
        #     b.next = a           # second node points to first

        #     prev = a             # advance prev to end of swapped pair

        # return dummy.next
        # prev, current = head, head.next
        # while current.next and current.next.next:
        #     prev.value, current.value = current.value, prev.value
        #     prev, current = prev.next.next, current.next.next
        # return head
        dummy = Node(None)
        dummy.next = head
        prev, current = dummy, dummy.next
        while prev.next and prev.next.next:
            next = current.next  # save Node(2)
            prev.next = next  # dummy -> 2
            current.next = next.next  # 1 -> 3
            next.next = current  # 2 -> 1
            prev, current = current, current.next  # prev=Node(1), current=Node(3)
        return dummy.next

    def printList(self, head):
        result = []
        current = head
        while current:
            result.append(str(current.value))
            current = current.next
        print(" -> ".join(result))


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    sol = Solution()
    # print("Original Linked List:")
    # sol.printList(head)

    ll = sol.swapPairs(head)
    print("After swapping pairs:")
    sol.printList(ll)
