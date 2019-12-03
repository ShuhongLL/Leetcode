class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        cur = 0
        for path in input.split('\n'):
            n = path.count('\t')
            while len(stack) > n:
                stack.pop()
            path = path[n:]
            if '.' in path:
                cur = max(cur, len('/'.join(stack + [path])))
            else:
                stack.append(path)
        return cur
