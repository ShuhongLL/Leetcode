class Solution:
    # solution: bfs + greedy
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        memo = [[0,3,2,3,2], [3,2,1,2,3], [2,1,4,3,2], [3,2,3,2,3], [2,3,2,3,4]]
        count = 0
        while x > 4 or y > 4:
            if x >= y:
                x -= 2
                y = y - 1 if y > 0 else y + 1
            else:
                y -= 2
                x = x - 1 if x > 0 else x + 1
            count += 1
        return count + memo[x][y]
