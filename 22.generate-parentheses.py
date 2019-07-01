#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def recursive(n: int, m: int, path: str) -> None:
            if n != 0:
                recursive(n - 1, m + 1 , path + '(')
                if m != 0:
                    recursive(n, m - 1, path + ')')
            else:
                if m != 0:
                    recursive(n, m - 1, path + ')')
                else:
                    result.append(path)
        recursive(n, 0, '')
        return result

