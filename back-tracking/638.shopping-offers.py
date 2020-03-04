class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.memo = {}
        return self.backtracking(price, special, needs)
    
    def backtracking(self, price: List[int], special: List[List[int]], needs: List[int]):
        key = tuple(needs)
        if key in self.memo:
            return self.memo[key]
        result = self.sumPrice(price, needs)
        for spec in special:
            cneeds = needs[::]
            for i in range(len(needs)):
                remain = cneeds[i] - spec[i]
                if remain < 0:    break
                cneeds[i] = remain
            else:
                result = min(result, spec[-1] + self.backtracking(price, special, cneeds))

        self.memo[key] = result
        return result
       
    def sumPrice(self, price: List[int], needs: List[int]):
        result = 0
        for i in range(len(price)):
            result += (price[i] * needs[i])
        return result