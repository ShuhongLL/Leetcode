class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        own_stock: keep the current stock (do nothing) / buy
        sell: sell all current own_stock
        no_action: do nothing (own no stock) / last step sold all stock hence cooldown
        """
        own_stock, sell, no_action = float('-inf'), 0, 0
        for price in prices:
            own_stock, sell, no_action = max(no_action - price, own_stock), own_stock + price, max(no_action, sell)
        return max(sell, no_action)
