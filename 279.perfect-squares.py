class Solution:
    def numSquares(self, n: int) -> int:
#   solution 1: dp  4000 ms
#         squares = [i**2 for i in range(1, int(n**.5)+1)]
#         dp = [float('inf')] * (n+1)
#         dp[0] = 0
        
#         for i in range(1, n+1):
#             for square in squares:
#                 if square > i:
#                     break
#                 dp[i] = min(dp[i], dp[i-square] + 1)
#         return dp[-1]

#   solution 2: greedy algorithm + bfs
        squares = [i**2 for i in range(1, int(n**.5)+1)]
        level = 0
        queue = [n]
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square in squares:
                    if remainder == square:
                        return level
                    elif square > remainder:
                        break
                    else:
                        next_queue.add(remainder - square)
            queue = list(tuple(next_queue))
