#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for ch in tokens:
            if ch in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                num = self._eval(ch, num1, num2)
                stack.append(num)
            else:
                stack.append(int(ch))
        return stack.pop()

    def _eval(self, op, num1, num2):
        if op == '+':
            return num1 + num2
        if op == '-':
            return num1 - num2
        if op == '*':
            return num1 * num2
        if op == '/':
            return int(num1 / num2)
# @lc code=end

