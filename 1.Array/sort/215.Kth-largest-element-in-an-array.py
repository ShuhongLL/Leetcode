import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        # runtime: nlogk
        # space: k
        for num in nums:
            if not queue:
                heapq.heappush(queue, num)
            elif len(queue) < k:
                heapq.heappush(queue, num)
            elif num > queue[0]:
                heapq.heappush(queue, num)
                heapq.heappop(queue)
        return queue[0]
