# Problem: https://leetcode.com/problems/counting-bits/
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = [0]*(n+1)
        for i in range(n+1):
            l[i] = format(i,"b").count("1")
        return l

if __name__ == "__main__":
    print(Solution().countBits(5))