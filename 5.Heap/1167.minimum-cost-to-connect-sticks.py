import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        result = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            cur = heapq.heappop(sticks)
            cur += heapq.heappop(sticks)
            heapq.heappush(sticks, cur)
            result += cur
        return result
