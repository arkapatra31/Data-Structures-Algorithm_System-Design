from typing import Counter, List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_counter = Counter(nums)
        for num, count in num_counter.items():
            if count == 1:
                return num
            
if __name__ == "__main__":
    print(Solution().singleNumber([2,2,-1]))