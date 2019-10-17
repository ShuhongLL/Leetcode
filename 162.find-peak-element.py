#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max = nums[0]
        for i in nums:
            if i > max:
                max = i
        return nums.index(max)
# @lc code=end

