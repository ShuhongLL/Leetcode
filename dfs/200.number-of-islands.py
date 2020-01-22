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
        result = 0
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == '1':
                    result += 1
                    self.bfs(row, col)
        return result


    def bfs(self, row: int, col: int):
        if row < 0 or row >= self.rows:
            return
        if col < 0 or col >= self.cols:
            return
        if self.grid[row][col] != '1':
            return
        self.grid[row][col] = '#'
        self.bfs(row-1, col)
        self.bfs(row+1, col)
        self.bfs(row, col-1)
        self.bfs(row, col+1)

# @lc code=end

