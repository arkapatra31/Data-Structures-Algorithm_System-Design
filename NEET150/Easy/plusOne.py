from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(str(x) for x in digits)) + 1
        a = []
        a.extend([int(digit) for digit in str(num)])
        return a
    
if __name__ == "__main__":
    print(Solution().plusOne([9,9]))