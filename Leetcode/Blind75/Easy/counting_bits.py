from typing import List
from collections import Counter

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = [0]*(n+1)
        for i in range(n+1):
            l[i] = format(i,"b").count("1")
        return l

if __name__ == "__main__":
    print(Solution().countBits(2))