class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N+1)
        dp[0] = True
        if N <= 1:
            return dp[N]
        dp[2] = True
        if N <= 2:
            return dp[N]
        for i in range(3, N+1):
            for num in range(1, i):
                if i % num == 0 and dp[num]:
                    dp[i] = True
                    break
        return dp[-1]
