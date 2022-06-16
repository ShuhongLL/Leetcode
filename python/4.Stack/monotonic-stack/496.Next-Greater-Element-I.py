class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonic stack: next greater number
        memo = {}
        stack = []
        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop(-1)
            memo[num] = stack[-1] if stack else -1
            stack.append(num)
        result = [0] * len(nums1)
        for i in range(len(nums1)):
            result[i] = memo[nums1[i]]
        return result