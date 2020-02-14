class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 30)
        prev = 0
        for i in range(30, days[-1] + 30):
            if i-30+1 in days:
                dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])
            else:
                dp[i] = prev
            prev = dp[i]
        return dp[-1]
