#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_max, cur_min, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            tmp1 = num * cur_max
            tmp2 = num * cur_min
            cur_max = max(tmp1, tmp2, num)
            cur_min = min(tmp1, tmp2, num)
            res = max(res, cur_max)
        return res
# @lc code=end

