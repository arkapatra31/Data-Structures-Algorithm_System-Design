class Stack:
    def __init__(self):
        self.items = []

    # Push an element onto the stack
    def push(self, element):
        self.items.append(element)

    # Pop an element off the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    # Peek the top element of the stack without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get the size of the stack
    def size(self):
        return len(self.items)

    # String representation of the stack
    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        return '\n'.join(map(str, reversed(self.items)))

    # Clear all elements from the stack
    def clear(self):
        self.items = []

# Example usage
my_stack = Stack()
my_stack.push(5)
my_stack.push(8)
my_stack.push(9)
my_stack.push(10)

print(my_stack)  # Print the stack (from top to bottom)
print(my_stack)  # Print again to verify state hasn't changed

# Uncomment the following lines to test other methods:
# print(my_stack.peek())     # 10
# my_stack.pop()
# print(my_stack.peek())     # 9
# print(my_stack.is_empty()) # False
# print(my_stack.size())     # 3
# my_stack.clear()
# print(my_stack.is_empty()) # True
