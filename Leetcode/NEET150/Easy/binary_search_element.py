
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        index = -1
        while start >= 0 and end < len(nums) and start <=end:
            mid = (start+end)//2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return index
            
if __name__ == "__main__":
    # Output: 4
    print(Solution().search([-1,0,3,5,9,12], 7))