# Problem : https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        if self.stack:
            top_value = self.stack.pop()
            if top_value == self.min_stack[-1]:
                self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())  # Returns -3
    min_stack.pop()
    print(min_stack.top())     # Returns 0
    print(min_stack.getMin())  # Returns -2