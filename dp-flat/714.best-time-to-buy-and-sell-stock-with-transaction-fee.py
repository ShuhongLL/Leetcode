class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        stack, no_stack = -prices[0], 0
        for price in prices[1:]:
            no_stack, stack = max(no_stack, stack + price - fee), max(stack, no_stack - price)
            # no need to consider sell and buy at same day:
            #   sell and buy:   stack + price - fee - price
            #   which is stack - fee < stack
        return max(stack, no_stack)
