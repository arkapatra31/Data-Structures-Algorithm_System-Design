class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s[0:2] if s[0] == s[1] else s[0]
        for i in range(len(s)):
            # Check odd-length palindromes (center at i)
            left, right = i, i
            length, res = self.__expand_from_center(s, length, res, left, right)
            
            # Check even-length palindromes (center between i and i+1)
            left, right = i, i + 1
            length, res = self.__expand_from_center(s, length, res, left, right)
        return res

    def __expand_from_center(self, s, length, res, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) >= length:
                length = (right - left + 1)
                res = s[left:right+1]
            left -= 1
            right += 1
        return length, res

if __name__ == "__main__":
    print(Solution().longestPalindrome("abb"))