def isValid(s: str) -> bool:
    # Dictionary to map closing brackets to opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []

    # Traverse the string
    for char in s:
        if char in mapping:
            # If closing bracket, check stack top
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            # If opening bracket, push to stack
            stack.append(char)

    # Valid if stack is empty
    return not stack


if __name__ == "__main__":
    print(isValid("([{(())}])"))
