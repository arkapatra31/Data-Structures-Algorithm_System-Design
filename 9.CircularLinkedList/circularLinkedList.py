class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = ""
        if self.length == 0:
            return "Empty Circular Linked List"
        while current is not self.tail:
            result += str(current.value)
            current = current.next
            result += " -> "
        result += str(self.tail.value)
        result += " -> " + str(self.head.value)
        return result

    def append(self, value):
        if self.length == 0:
            new_node = Node(value)
            self.head, self.tail = new_node, new_node
            self.tail.next = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
            self.tail.next = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            self.length += 1
        return True

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.append(value)
            else:
                self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1
        return True

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break
        return True

    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.head
        elif index == self.length - 1:
            return self.tail
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            self.head.value = value
        elif index == self.length - 1:
            self.tail.value = value
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.value = value
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node.value
        else:
            popped_node = self.head
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
            self.length -= 1
            return popped_node.value

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            popped_node.next = None
            self.head, self.tail = None, None
            self.length = 0
            return popped_node.value
        else :
            popped_node = self.tail
            current = self.head
            while current.next is not self.tail:
                current = current.next
                print(f"Current: {current.value}")
            current.next = popped_node.next
            self.tail = current
            popped_node.next = None
            self.length -= 1
            return popped_node.value

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            target_node = self.get_node(index-1)
            removed_node = self.get_node(index)
            target_node.next = self.get_node(index+1)
            removed_node.next = None
            self.length -= 1
        return True

    def delete_all(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head, self.tail = None, None
            self.length = 0
        else:
            self.tail.next = None  # Tail to point to None to break the circular link
            self.head, self.tail = None, None
            self.length = 0
        return True
            


if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(34)
    cll.append(25)
    cll.append(67)
    print(f"CLL after appending: {cll}")
    cll.prepend(90)
    print(f"CLL after prepending 0: {cll}")
    print(f"Length: {cll.length}")
    cll.insert(4, 100)
    print(f"CLL after inserting 10: {cll}")
    print(f"Length: {cll.length}")
    cll.insert(4, 110)
    print(f"CLL after inserting 11: {cll}")
    print(f"Index of 11: {cll.search(11)}")
    print(f"Node at index 3: {cll.get_node(3)}")
    print(f"Setting value at index 3 to 1000: {cll.set_value(3, 1000)}")
    print(f"CLL after setting value: {cll}")
    print(f"Popping first node: {cll.pop_first()}")
    print(f"CLL after popping first node: {cll}")
    print(f"Popping last node: {cll.pop()}")
    print(f"CLL after popping last node: {cll}")
    print(f"Removing node at index 1: {cll.remove(1)}")
    print(f"CLL after removing node at index 1: {cll}")
    print(f"Deleting all nodes: {cll.delete_all()}")
    print(f"CLL after deleting all nodes: {cll}")
    # cll.traverse()
