class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        return s == s[::-1]

if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))