from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Will store indices of elements in the current window
        result = []
        left = right = 0
        while right < len(nums):
            # Pop smaller elements from the right — they can never be the max as the queue will be in decreasing order
            # this is called "monotonic queue" technique
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)  # Add current index to the queue

            # Remove left if it's outside the current window
            if left > dq[0]:
                dq.popleft()

            if right + 1 >= k:  # We have a valid window
                result.append(nums[dq[0]])  # Front of queue is the max for this window
                left += 1  # Shrink window from the left
            right += 1  # Expand window to the right

        return result


if __name__ == "__main__":
    print("=== Sliding Window Maximum Demo ===\n")
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))  # Expected: [3,3,5,5,6,7]