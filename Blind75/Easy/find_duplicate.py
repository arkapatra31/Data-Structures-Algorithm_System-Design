from typing import Counter, List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        return False

if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10,1]
    print(Solution().containsDuplicate([1,2,3,4,5,6,7,8,9,10,1]))