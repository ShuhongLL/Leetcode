class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        result = [0] * 3
        for cost in costs:
            result = [cost[i] + min(result[(i+1)%3], result[(i+2)%3]) for i in range(3)]
        return min(result)
