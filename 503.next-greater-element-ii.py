#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
import collections

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

#   method 1: brute force
#         result = []
#         stack = collections.deque([])
#         i = 0
#         size = len(nums)
        
#         while i < size:
#             cur = 0
#             while cur < size:
#                 if cur == len(stack):
#                     stack.append(nums[(cur + i) % size])
#                 if stack[cur] > stack[0]:
#                     result.append(stack[cur])
#                     stack.popleft()
#                     break
#                 cur += 1
#             else:
#                 result.append(-1)
#                 stack.popleft()
#             i += 1
#         return result

#   method 2: back tracking + stack
        stack = []
        result = [-1] * len(nums)
        for i in range(len(nums)*2, 0, -1):
            index = i % len(nums) - 1
            if not stack:
                stack.append(nums[index])
            else:
                while stack:
                    if stack[-1] > nums[index]:
                        result[index] = stack[-1]
                        break
                    else:
                        stack.pop()
                stack.append(nums[index])
        return result

# @lc code=end

