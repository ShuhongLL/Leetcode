#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
import collections

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.board = board
        for row in range(len(board)):
            for column in range(len(board[row])):
                if row == 0 or column == 0 or row == len(board)-1 or column == len(board[row])-1:
                    self.dfs(row, column)
        
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == '#':
                    board[row][column] = 'O'
                else:
                    board[row][column] = 'X'

    def dfs(self, row: int, column: int):
        if (row < 0 or column < 0 or row >= len(self.board) or column >= len(self.board[row]) or self.board[row][column] == 'X'):
            return
        if self.board[row][column] == '#':
            return
        self.board[row][column] = '#'
        self.dfs(row-1, column)
        self.dfs(row, column-1)
        self.dfs(row+1, column)
        self.dfs(row, column+1)
    
# @lc code=end

