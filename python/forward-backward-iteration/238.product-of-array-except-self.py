#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from operator import mul
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        for i in range(1, length):
            result[i] = result[i-1] * nums[i-1]
        r_product = 1
        for i in reversed(range(length)):
            result[i] = result[i] * r_product
            r_product *= nums[i]
        return result      
# @lc code=end

