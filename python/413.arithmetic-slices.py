class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # dp solution:
        if len(A) < 3:
            return 0
        dp = [0] * len(A)
        result = 0
        for i in range(2, len(A)):
            if A[i-1] - A[i-2] == A[i] - A[i-1]:
                dp[i] = dp[i-1] + 1
                result += dp[i]
        return result
