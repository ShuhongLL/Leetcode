import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        heap = []
        rooms = 0
        intervals.sort()
        for i in range(len(intervals)):
            if len(heap) == 0:
                rooms += 1
                heapq.heappush(heap, intervals[i][1])
            else:
                if heap[0] <= intervals[i][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, intervals[i][1])
                else:
                    rooms += 1
                    heapq.heappush(heap, intervals[i][1])
        return rooms