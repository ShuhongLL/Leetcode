class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result, min_p = 0, float('inf')
        for price in prices:
            result = max(result, price - min_p)
            min_p = min(min_p, price)
        return result
