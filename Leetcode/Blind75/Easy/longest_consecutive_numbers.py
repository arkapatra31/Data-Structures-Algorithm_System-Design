# Problem: https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

# Method to find the number of longest consecutive numbers present in the list
class Solution:
    def longestConsecutive(nums: List[int]) -> int:
        nl = list(set(nums))
        nl.sort()
        if len(nl) == 1:
            return 1
        if len(nl) == 0:
            return 0
        
        count, max_count = 1,1
        for x in range(1, len(nl)):
            if nl[x] - nl[x-1] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count

nums = [100,4,200,1,3,2]
#nums = [1,100]
print(Solution.longestConsecutive(nums))  # Returns 4