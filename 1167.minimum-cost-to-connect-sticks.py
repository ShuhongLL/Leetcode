import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        result, cur = 0, 0
        while len(sticks) > 1:
            cur += heapq.heappop(sticks)
            cur += heapq.heappop(sticks)
            heapq.heappush(sticks, cur)
            result += cur
            cur = 0
        return result
