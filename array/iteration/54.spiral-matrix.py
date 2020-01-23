#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        first_row, first_col = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        result = []
        while rows > 0 and cols > 0:
            last_row = first_row + rows - 1
            last_col = first_col + cols - 1

            result += [matrix[first_row][i] for i in range(first_col, last_col+1)]
            result += [matrix[i][last_col] for i in range(first_row+1, last_row+1)]
            # note: last_row may equal to first_row, result as duplication
            if first_row != last_row:
                result += [matrix[last_row][i] for i in range(last_col-1, first_col-1, -1)]
            # note: last_col may equal to first_col, result as duplication
            if first_col != last_col:
                result += [matrix[i][first_col] for i in range(last_row-1, first_row, -1)]
            first_row += 1
            first_col += 1
            rows -= 2
            cols -= 2
        return result

