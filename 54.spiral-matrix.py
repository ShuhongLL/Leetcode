#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # edge:
        if not matrix:
            return []

        firstRow, firstCol = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        result = []

        while rows > 0 and cols > 0:
            lastRow = firstRow + rows - 1
            lastCol = firstCol + cols - 1

            for i in range(cols):
                result.append(matrix[firstRow][firstCol + i])
            for i in range(1, rows):
                result.append(matrix[firstRow + i][lastCol])
            for i in range(1, cols):
                if firstRow != lastRow:
                    result.append(matrix[lastRow][lastCol - i])
            for i in range(1, rows - 1):
                if firstCol != lastCol:
                    result.append(matrix[lastRow - i][firstCol])
            firstRow += 1
            firstCol += 1
            rows -= 2
            cols -= 2

        return result
