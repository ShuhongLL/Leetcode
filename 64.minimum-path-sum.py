#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        column = len(grid) - 1
        row = len(grid[0]) - 1
        dicts = {}

        def walk(nums: List[List[int]], row: int, column: int, row_e: int, column_e: int) -> int:
            if row == row_e and column == column_e:
                return nums[column][row]
            key = str(row) + ':' + str(column)
            if key in dicts:
                return dicts[key]
            right, down = 99999999, 99999999
            if row < row_e:
                right = walk(nums, row + 1, column, row_e, column_e)
            if column < column_e:
                down = walk(nums, row, column + 1, row_e, column_e)
            cur = nums[column][row] + min(right, down)
            dicts[key] = cur
            return cur
        
        return walk(grid, 0, 0, row, column)

