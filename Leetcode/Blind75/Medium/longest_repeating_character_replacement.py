# Problem : https://leetcode.com/problems/longest-repeating-character-replacement/description/
# You are given a string s and an integer k. You can choose any character of the string and change 
# it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(max_freq, char_count[s[right]])

            # If the current window size minus the count of the most frequent character is greater than k,
            # it means we need to shrink the window from the left.
            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

        return len(s) - left
    
if __name__ == "__main__":
    s = "ABAB"
    k = 1
    print(Solution().characterReplacement(s, k))  # Output: 3 (the longest substring is "AAA" or "BBB" after one replacement)



# Strategy: Sliding Window
# 1. We maintain a sliding window defined by two pointers, left and right.
# 2. We keep track of the frequency of characters in the current window using a dictionary
# 3. We also keep track of the maximum frequency of any character in the current window
# 4. If the size of the current window minus the maximum frequency is greater than k
#    (meaning we would need to change more than k characters to make all characters the same
#    in the window), we shrink the window from the left.