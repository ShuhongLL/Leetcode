#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(word, i, j):
                    return True
        return False
  
    def search(self, word, i, j):
        # found word
        if len(word) == 0:
            return True
        
        # out of bounds or has visited already
        if i < 0 or i >= len(self.board) or j < 0 or j >= len(self.board[0]) or (i, j) in self.visited:
            return False
        
        # invalid word, go back
        if self.board[i][j] != word[0]:
            return False
        
        # add to visited set
        self.visited.add((i, j))
        
        # search neighbors
        found = self.search(word[1:], i+1, j) or \
                self.search(word[1:], i, j+1) or \
                self.search(word[1:], i-1, j) or \
                self.search(word[1:], i, j-1)
        
        # remove from visited set, if needed
        if not found:
            self.visited.remove((i, j))

        return found
