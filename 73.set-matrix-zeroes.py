#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        column = set()
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                row.add(i)
                column |= set([n for (n, v) in enumerate(matrix[i]) if v == 0])
        for i in range(len(matrix)):
            if i in row:
                matrix[i] = [0 for n in matrix[i]]
            for m in column:
                matrix[i][m] = 0
