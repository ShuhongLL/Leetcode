class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0, 0] + cost
        dp = [float('inf')] * (len(cost))
        dp[0], dp[1] = 0, 0
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])
