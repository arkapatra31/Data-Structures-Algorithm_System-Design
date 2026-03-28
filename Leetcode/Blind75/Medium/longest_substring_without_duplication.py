class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char_map = {}  # Stores the last seen index of each character
        # max_length = 0
        # start = 0      # Left boundary of the sliding window

        # for end, char in enumerate(s):
        #     # If char is already in the current window, move start past it
        #     if char in char_map and char_map[char] >= start:
        #         start = char_map[char] + 1
            
        #     # Update last seen index and calculate current window size
        #     char_map[char] = end
        #     max_length = max(max_length, end - start + 1)
            
        # return max_length
        n = len(s)
        cset = set()
        maxLen = 0
        left = 0
        for right in range(n):
            while s[right] in cset:
                cset.remove(s[left])
                left += 1
            print(left,right, cset)
            cset.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen

    # def longestSubstringWithoutDuplication(self, s: str) -> int:
    #     char_map = {}
    #     start = 0
    #     max_start = 0
    #     max_len = 0

    #     for end, char in enumerate(s):
    #         # Move the start pointer if we find a duplicate in the current window
    #         if char in char_map and char_map[char] >= start:
    #             start = char_map[char] + 1
            
    #         char_map[char] = end
            
    #         # Check if the current window is the longest we've seen
    #         if (end - start + 1) > max_len:
    #             max_len = end - start + 1
    #             max_start = start

    #     return s[max_start : max_start + max_len]
        

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    #print(Solution().longestSubstringWithoutDuplication("abcabcdbb"))