class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        print(dp)
        dp[1] = 1
        dp[2] = 2
        for steps in range(3, n + 1):
            dp[steps] = dp[steps - 1] + dp[steps - 2]
        return dp[n]


print(Solution().climbStairs(3))