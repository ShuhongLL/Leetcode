import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        queue = []
        rooms = 0
        for i in range(len(intervals)):
            if not queue:
                queue.append(intervals[i][1])
                rooms += 1
            else:
                # end before next meeting start
                if queue[0] <= intervals[i][0]:
                    heapq.heappop(queue)
                    heapq.heappush(queue, intervals[i][1])
                else:
                    heapq.heappush(queue, intervals[i][1])
                    rooms += 1
        return rooms
