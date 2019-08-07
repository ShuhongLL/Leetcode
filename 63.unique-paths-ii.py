#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) - 1
        n = len(obstacleGrid[0]) - 1

        dicts = {}

        def walk(nums: List[List[int]], row: int, column: int, row_e: int, col_e: int) -> int:
            if nums[column][row] == 1:
                return 0
            if row == row_e and column == col_e:
                return 1
            key = str(row) + ':' + str(column)
            if key in dicts:
                return dicts[key]
            right = 0
            down = 0
            if row < row_e:
                right = walk(nums, row + 1, column, row_e, col_e)
            if column < col_e:
                down = walk(nums, row, column + 1, row_e, col_e)
            dicts[key] = right + down
            return dicts[key]
        return walk(obstacleGrid, 0, 0, n, m)

