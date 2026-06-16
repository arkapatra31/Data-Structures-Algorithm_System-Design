# Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List

class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     a = []
    #     start = 0
    #     end = len(nums) - 1
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if nums[mid] == target:
    #             a.append(mid)
    #             left = mid - 1
    #             while left >= 0 and nums[left] == target:
    #                 a.append(left)
    #                 left -= 1
    #             right = mid + 1
    #             while right < len(nums) and nums[right] == target:
    #                 a.append(right)
    #                 right += 1
    #             break
    #         elif nums[mid] < target:
    #             start = mid + 1
    #         else:
    #             end = mid - 1
    #     if not a:
    #         return [-1, -1]
    #     return [min(a), max(a)]
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        count = nums.count(target)
        if count == 0:
            return [-1, -1]
        start = nums.index(target)
        for i in range(start, len(nums)):
            if nums[i] == target:
                end = i
        return [start, end]
if __name__ == "__main__":
    # Output: [3,4]
    print(Solution().searchRange([5,6,7,8,5,5,9], 5))