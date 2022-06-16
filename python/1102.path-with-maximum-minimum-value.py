import heapq

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
    # intent to make every step chosing those maximum numbers
    # so that the minimum value of the whole path
    # will be the maximum over possible paths
        row, col = len(A), len(A[0])
        seen = {}
        seen[0, 0] = None
        q = []
        heapq.heappush(q, (-A[0][0], 0, 0))
        minimum = A[0][0]
        while q:
            val, x, y = heapq.heappop(q)
            minimum = min(minimum, -val)
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                a, b = x+dx, y+dy
                if a >= 0 and a < row and b>= 0 and b < col and (a, b) not in seen:
                    if a == row-1 and b == col-1:
                        return min(A[row-1][col-1], minimum)
                    heapq.heappush(q, (-A[a][b], a, b))
                    seen[a, b] = None
        return -1
