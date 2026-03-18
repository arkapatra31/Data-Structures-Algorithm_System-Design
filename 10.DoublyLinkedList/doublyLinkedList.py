from hmac import new
from unittest import result


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.value})"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.length == 0:
            return "Empty Doubly Linked List"
        else:
            result = ""
            current = self.head
            while current is not None:
                result += str(current.value)+"<->"
                current = current.next
            return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            current_node = self.tail
            current_node.next = new_node
            new_node.prev = current_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            current = self.head
            current.prev = new_node
            new_node.next = current
            self.head = new_node
        self.length += 1
        return True

    def traverse(self):
        if self.length == 0:
            print("Empty Doubly Linked List")
        else:
            result = ""
            current = self.head
            while current:
                result += str(current.value)+"<->"
                current = current.next
            return result

    def reverse_traverse(self):
        if self.length == 0:
            print("Empty Doubly Linked List")
        else:
            result = ""
            current = self.tail
            while current:
                result += f"{current.value}<->"
                current = current.prev
            return result

    def search(self, value):
        if self.length == 0:
            return None
        else:
            current = self.head
            while current:
                if current == value:
                    return True
                current = current.next
            return True

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head
        elif index == self.length - 1:
            return self.tail
        else:
            if index <= self.length // 2:
                current = self.head
                for _ in range(index):
                    current = current.next
                return current
            else:
                current = self.tail
                for _ in range(self.length - 1 - index):
                    current = current.prev
                return current

    def set(self, index, value):
        # new_node = Node(value)
        # if index < 0 or index >= self.length:
        #     return None
        # elif index == 0:
        #     next_node = self.head.next
        #     next_node.prev = new_node
        #     new_node.next = next_node
        #     self.head = new_node
        # elif index == self.length - 1:
        #     prev_node = self.tail.prev
        #     prev_node.next = new_node
        #     new_node.prev = prev_node
        #     self.tail = new_node
        # else:
        #     old_node = self.get_node(index)
        #     prev_node = old_node.prev
        #     next_node = old_node.next
        #     prev_node.next = new_node
        #     new_node.prev = prev_node
        #     new_node.next = next_node
        #     next_node.prev = new_node
        #     old_node.next, old_node.prev = None, None
        #     return True

        node = self.get_node(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        old_node = self.get_node(index)
        if old_node:
            prev_node = old_node.prev
            new_node.prev, new_node.next = prev_node, old_node
            prev_node.next, old_node.prev = new_node, new_node
            self.length += 1
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.length -= 1
            return current

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            current = self.tail
            self.head, self.tail = None, None
            self.length = 0
            return current
        else:
            current = self.tail
            self.tail = current.prev
            current.prev, current.next = None, None
            self.length -= 1
            return current

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        old_node = self.get_node(index)
        if old_node:
            prev_node = old_node.prev
            next_node = old_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            old_node.next, old_node.prev = None, None
            self.length -= 1
            return old_node
        return False

    def delete_all(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head, self.tail = None, None
            self.length = 0
            return True
        else:
            # Method 1 ( GC will clear up eventually)
            # self.head, self.tail = None, None

            # Method 2 (Breaking the links between each nodes)
            current = self.head
            while current:
                next_node = current.next
                current.prev, current.next = None, None
                current = next_node
            self.length = 0
            return True

if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(78)
    doubly_linked_list.append(90)
    doubly_linked_list.append(1098)
    doubly_linked_list.append(56)
    print(doubly_linked_list)
    doubly_linked_list.prepend(22)
    print(f"After prepending 22: {doubly_linked_list}")
    doubly_linked_list.prepend(31)
    print(f"After prepending 31: {doubly_linked_list}")
    print(f"Traversing : {doubly_linked_list.traverse()}")
    #print(f"ReverseTraversing : {doubly_linked_list.reverse_traverse()}")
    print(f"Node with value 90 present : {doubly_linked_list.search(90)}")
    print(f"Get Node in index 4 : {doubly_linked_list.get_node(4)}")
    doubly_linked_list.set(3, 100)
    print(f"After setting node in index 3 to 100: {doubly_linked_list}")
    doubly_linked_list.insert(2, 89)
    print(f"After inserting 89 at index 2: {doubly_linked_list}")
    print(f"Popping first node: {doubly_linked_list.pop_first()}")
    print(f"After popping first node: {doubly_linked_list}")
    print(f"Popping last node: {doubly_linked_list.pop()}")
    print(f"After popping last node: {doubly_linked_list}")
    print(f"Removing node at index 2: {doubly_linked_list.remove(2)}")
    print(f"After removing node at index 2: {doubly_linked_list}")
    print(f"Deleting all nodes: {doubly_linked_list.delete_all()}")
    print(f"After deleting all nodes: {doubly_linked_list}")