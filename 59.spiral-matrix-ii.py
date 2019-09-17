#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        firstRow, firstCol = 0, 0
        row, column = n, n
        while row > 0 and column > 0:
            lastRow = firstRow + row - 1
            lastCol = firstCol + column - 1
            for i in range(column):
                result[firstRow][firstCol + i] = count
                count += 1
            for i in range(1, row):
                result[firstRow + i][lastCol] = count
                count += 1
            for i in range(1, column):
                result[lastRow][lastCol - i] = count
                count += 1
            for i in range(1, row - 1):
                result[lastRow - i][firstCol] = count
                count += 1
            firstRow += 1
            firstCol += 1
            row -= 2
            column -= 2
        return result
