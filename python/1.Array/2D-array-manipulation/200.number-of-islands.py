#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(row: int, col: int, rows: int, cols: int):
            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return
            if grid[row][col] != '1':
                return
            grid[row][col] = '#'
            bfs(row-1, col, rows, cols)
            bfs(row+1, col, rows, cols)
            bfs(row, col-1, rows, cols)
            bfs(row, col+1, rows, cols)

        result = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    result += 1
                    bfs(row, col, rows, cols)
        return result

# @lc code=end
