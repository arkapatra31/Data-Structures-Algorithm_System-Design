from typing import List

# Method to find the number of longest consecutive numbers present in the list
def longestConsecutive(nums: List[int]) -> int:
    nl = list(set(nums))
    nl.sort()
    if len(nl) == 1:
        return 1
    if len(nl) == 0:
        return 0
    
    count, max_count = 1,1
    for x in range(len(nl)):
        if nl[x] - nl[x-1] == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1
    return max_count

#nums = [100,4,200,1,3,2]
nums = [1,100]
print(longestConsecutive(nums))