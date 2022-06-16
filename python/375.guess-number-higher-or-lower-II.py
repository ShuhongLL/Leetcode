class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp solution:
        # memo[i][j] represents the result for subsequence [i:j]
        memo = [[0] * (n+1) for _ in range(n+1)]
        for length in range(1, n):
            for i in range(1, n - length + 1):
                v = min(m + max(memo[i][m-1], memo[m+1][i+length]) for m in range(i, i+length))
                memo[i][i + length] = v
        return memo[1][n]
