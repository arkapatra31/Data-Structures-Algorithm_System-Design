# Problem : https://leetcode.com/problems/palindromic-substrings/?envType=problem-list-v2&envId=oizxjoit

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.count_palindrome(s, i, i) # odd length
            count += self.count_palindrome(s, i, i+1) # even length
        return count

    def count_palindrome(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    s = "abc"
    print(solution.countSubstrings(s))  # Output: 3


# Strategy to solve the problem:
# 1. Initialize a count variable to keep track of the number of palindromic substrings.
# 2. Iterate through each character in the string as a potential center of a palindrome.
# 3. For each character, expand outwards to check for palindromic substrings of both odd and even lengths.
# 4. Use a helper function to count palindromic substrings by expanding from the center 
#    and checking for equality of characters on both sides.  