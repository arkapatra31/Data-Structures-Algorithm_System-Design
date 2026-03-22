from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        area = 0
        while left < right:
            area = max(area, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

if __name__ == "__main__":
    height = [4,3,2,1,4]
    print(Solution().maxArea(height))