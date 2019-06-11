#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arrSum = maxSum = nums[0]
        for num in nums[1:]:
            arrSum = max(num, arrSum + num)
            maxSum = max(maxSum, arrSum)
        return maxSum

