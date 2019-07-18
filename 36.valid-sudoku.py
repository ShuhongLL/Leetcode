#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDicts = {}
        colDicts = {}
        gridDicts = {}
        for row_i in range(0, 9):
            for col_i in range(0, 9):
                p_v = board[row_i][col_i]
                if p_v != ".":
                    if (p_v + str(row_i)) in rowDicts or (p_v + str(col_i)) in colDicts or (p_v + str(row_i // 3) + str(col_i // 3)) in gridDicts:
                        return False
                    rowDicts[p_v + str(row_i)] = 1
                    colDicts[p_v + str(col_i)] = 1
                    gridDicts[p_v + str(row_i // 3) + str(col_i // 3)] = 1
        return True
