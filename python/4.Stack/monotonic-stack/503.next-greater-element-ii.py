class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 循环数组：取两倍长度，每次遍历 idx取模值
        # monotonic stack: next greater number
        stack = []
        result = [0] * len(nums)
        n = len(nums)
        for i in range(2*len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop(-1)
            result[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        return result
