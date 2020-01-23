#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.dfs(n, n, '')
        return self.result
        
    def dfs(self, bra: int, ket: int, path: str):
        if bra == 0:
            self.result.append(path + ')' * ket )
        else:
            self.dfs(bra - 1, ket, path + '(')
            if bra < ket:
                self.dfs(bra, ket - 1, path + ')')


