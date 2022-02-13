class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack: next greater number
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop(-1)
            result[i] = stack[-1][1] - i if stack else 0
            stack.append([temperatures[i], i])
        return result
