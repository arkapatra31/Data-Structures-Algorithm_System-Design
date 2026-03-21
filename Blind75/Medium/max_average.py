from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum, maxSum = 0, 0
        for i in range(k):
            sum += nums[i]
        
        maxSum = sum

        for i in range(k, len(nums)):
            sum += nums[i] - nums[i-k]
            maxSum = max(maxSum, sum)
        return maxSum / k
    
if __name__ == "__main__":
    print(Solution().findMaxAverage([1,12,-5,-6,50,3], 3))