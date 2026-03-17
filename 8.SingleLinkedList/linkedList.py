class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.node = Node(value)
        self.head = self.node
        self.tail = self.node
        self.length = 1

    # __str__ method is string representation of the class so we will override it to
    # return the string representation of the linked list
    def __str__(self) -> str:
        result = ""
        if self.length == 0:
            return "Empty Linked List"
        else:
            current = self.head
            while current is not None:
                result += f"{current.value}->"
                current = current.next
            result += "None"
            return result

    def append(self, value):
        print("Appending...")
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        print("Prepending...")
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        print(f"Inserting at index {index}...")
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            if self.length == 0:
                new_node = Node(value)
                self.head = new_node
                self.tail = new_node
            elif index < 0 or index > self.length:
                return False
            else:
                current = self.head
                for _ in range(index-1):
                    current = current.next
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def search(self, value):
        if self.length == 0:
            return False
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return True
                current = current.next
            return False

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.head.value
        else:
            i = 0
            current = self.head
            while i != index:
                current = current.next
                i+=1
            return current.value

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            self.head.value = value
            return True
        else:
            current = self.head
            _ = 0
            while _ != index:
                current = current.next
                _+=1
            current.value = value
            return True

    def pop_first(self):
        if self.length == 0:
            return False
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node
        else:
            current_head = self.head
            self.head = current_head.next
            current_head.next = None
            self.length -= 1
            return current_head

    def pop(self):
        if self.length == 0:
            return False
        elif self.length == 1:
            popped_node = self.head
            self.head, self.tail = None, None
            self.length = 0
            return popped_node
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            popped_node = current.next
            current.next = None
            self.tail = current
            self.length -= 1
            return popped_node

    
    def remove_node(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            popped_node: Node = current.next
            current.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def remove_all_nodes(self):
        if self.length == 0:
            return False
        else:
            self.head = None
            self.tail = None
            self.length = 0
            return True

if __name__ == "__main__":
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print(f"Before Prepend: {ll}")
    ll.prepend(10)
    print(f"After Prepend: {ll}")
    ll.prepend(20)
    print(f"After Prepend: {ll}")
    ll.insert(5, 50)
    print(f"After Insert: {ll}")
    ll.traverse()
    print(f"Search 20: {ll.search(20)}")
    print(f"Node at index 2: {ll.get_node(2)}")
    print(f"Setting value at index 2 to 100: {ll.set_value(2, 100)}")
    print(f"After setting value: {ll}")
    print(f"Popping first node: {ll.pop_first()}")
    print(f"After popping first node: {ll}")
    print(f"Popping last node: {ll.pop()}")
    print(f"After popping last node: {ll}")
    print(f"Removing node at index 2: {ll.remove_node(2)}")
    print(f"After removing node: {ll}")
    print(f"Removing all nodes: {ll.remove_all_nodes()}")
    print(f"After removing all nodes: {ll}")