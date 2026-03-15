# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

def find2sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
    
    # Below code also works but:-
    # index scan the list from beginning to end so it is time consuming
    # if target is 6 and nums is [3,4,8,9,2], then it will return [0,0] which is incorrect
    idx = []
    for num in nums:
        complement = target - num
        if complement in nums:
            idx.append(nums.index(num))
            idx.append(nums.index(complement))
            return idx
    return idx


nums = [11,15,5,4,3]
target = 8
print(find2sum(nums, target))