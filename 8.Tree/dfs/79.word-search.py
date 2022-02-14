#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word):
                    return True
        return False

    def dfs(self, board: List[List[str]], x: int, y: int, word: str):
        if not word:
            return True
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == '#':
            return False
        if board[x][y] != word[0]:
            return False

        prev = board[x][y]
        board[x][y] = '#'

        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in steps:
            a, b = x + dx, y + dy
            if self.dfs(board, a, b, word[1:]):
                board[x][y] = prev
                return True

        board[x][y] = prev
        return False
