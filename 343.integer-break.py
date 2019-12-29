class Solution:
    def integerBreak(self, n: int) -> int:
        # break to 3 as many as possible
        # 4 is the only exception
        if n <= 3:
            return 1 if n != 3 else 2
        dp = [1] * (n+1)
        dp[2], dp[3], dp[4] = 2, 3, 4
        for i in range(5, n+1):
            dp[i] = 3 * dp[i-3]
        return dp[-1]
