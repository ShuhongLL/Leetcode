class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = ['']
        num_stack = []
        for i in range(len(s)):
            if str.isalpha(s[i]):
                str_stack[-1] += s[i]
            elif s[i] == '[':
                str_stack.append('')
                num_stack.append(int(s[i-1]))
            elif s[i] == ']':
                num = num_stack.pop()
                cur = str_stack.pop()
                str_stack[-1] += (num * cur)
        return str_stack[-1]
