class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop(-1)
            elif s[i] == '[':
                stack.append(s[i])
            elif s[i] == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop(-1)
            elif s[i] == '{':
                stack.append(s[i])
            elif s[i] == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop(-1)
            else:
                return False
        return len(stack) == 0
