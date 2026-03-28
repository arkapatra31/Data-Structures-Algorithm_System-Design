from typing import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = format(n,'032b')
        bd = Counter(binary)
        return bd['1']
if __name__ == "__main__":
    print(Solution().hammingWeight(10))