class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:            
        # return max_length
        n = len(s)
        cset = set()
        maxLen = 0
        left = 0
        for right in range(n):
            while s[right] in cset:
                cset.remove(s[left])
                left += 1
            cset.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    #print(Solution().longestSubstringWithoutDuplication("abcabcdbb"))