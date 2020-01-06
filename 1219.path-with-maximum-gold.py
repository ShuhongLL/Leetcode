class Solution:
    # solution 1: backtracking
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    self.dfs(grid, i, j, grid[i][j])
        return self.result
    
    def dfs(self, grid: List[List[int]], row: int, col: int, gold: int):
        prev = grid[row][col]
        grid[row][col] = -1
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in steps:
            a, b = row + dx, col + dy
            if a >= 0 and b >= 0 and a < len(grid) and b < len(grid[0]) and grid[a][b] > 0:
                self.dfs(grid, a, b, gold + grid[a][b])
        grid[row][col] = prev
        self.result = max(self.result, gold)
