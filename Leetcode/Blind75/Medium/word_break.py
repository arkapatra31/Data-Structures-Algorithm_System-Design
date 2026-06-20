# Problem : https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=oizxjoit

from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @lru_cache(None)
        def dp(i):
            if i == len(s):
                return True
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in word_set and dp(j):
                    return True
            return False

        return dp(0)

if __name__ == "__main__":
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(Solution().wordBreak(s, wordDict))

# Time Complexity: O(n^2) where n is the length of the string s. This is because in the worst case, we may need to check all possible substrings of s.
# Space Complexity: O(n) due to the recursion stack and the memoization cache used by the lru_cache decorator.

# Strategy: We use a recursive approach with memoization to check if the string can be segmented into words from the dictionary.
# We define a helper function dp(i) that checks if the substring starting from index i can be segmented.
# We iterate through possible end indices j and check if the substring s[i:j] is in the word set and if dp(j) returns True.
# If we find a valid segmentation, we return True. If we exhaust all possibilities, we return False.
