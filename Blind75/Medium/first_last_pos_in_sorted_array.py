from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = []
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                a.append(mid)
                left = mid - 1
                while left >= 0 and nums[left] == target:
                    a.append(left)
                    left -= 1
                right = mid + 1
                while right < len(nums) and nums[right] == target:
                    a.append(right)
                    right += 1
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if not a:
            return [-1, -1]
        return [min(a), max(a)]
    
if __name__ == "__main__":
    # Output: [3,4]
    print(Solution().searchRange([1,0], 1))