class Solution:
    # stack + greedy
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
        return j == len(popped)
