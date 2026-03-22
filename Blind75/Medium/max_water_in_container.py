from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxNum = 0
        secondNum = 0
        for i in range(len(height)):
            if maxNum < height[i]:
                maxNum = height[i]
            
            if height[i] > secondNum and height[i] < maxNum:
                secondNum = height[i]
            
        if secondNum:
            return secondNum**2
        else:
            return maxNum**2

if __name__ == "__main__":
    height = [4,3,2,1,4]
    print(Solution().maxArea(height))