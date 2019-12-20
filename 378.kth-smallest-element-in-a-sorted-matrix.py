import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # heap solution:
        queue, seen = [], {}
        result = 0
        heapq.heappush(queue, (-matrix[-1][-1], len(matrix)-1, len(matrix[0])-1))
        total = len(matrix) * len(matrix[0])

        for _ in range(total - k + 1):
            result, row, col = heapq.heappop(queue)
            # Note: duplicate path
            if row > 0 and (row-1, col) not in seen:
                seen[row-1, col] = None
                heapq.heappush(queue, (-matrix[row-1][col], row-1, col))
            if col > 0 and (row, col-1) not in seen:
                seen[row, col-1] = None
                heapq.heappush(queue, (-matrix[row][col-1], row, col-1))
        return -result
