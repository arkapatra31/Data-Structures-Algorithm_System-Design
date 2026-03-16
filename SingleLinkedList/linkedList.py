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