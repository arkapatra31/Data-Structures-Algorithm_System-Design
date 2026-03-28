from typing import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> any:
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))