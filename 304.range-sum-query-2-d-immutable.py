#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.grid_map = {}
        if matrix:
            for i in range(len(matrix)):
                cur_sum = 0
                for j in range(len(matrix[0])):
                    cur_sum += matrix[i][j]
                    prev_sum = self.grid_map[(i-1, j)] if i != 0 else 0
                    self.grid_map[(i, j)] = prev_sum + cur_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.grid_map[(row2, col2)]
        top = self.grid_map[(row1-1, col2)] if (row1-1, col2) in self.grid_map else 0
        left = self.grid_map[(row2, col1-1)] if (row2, col1-1) in self.grid_map else 0
        top_left = self.grid_map[(row1-1, col1-1)] if (row1-1, col1-1) in self.grid_map else 0
        return total - top - left + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

