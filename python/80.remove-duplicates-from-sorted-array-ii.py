#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge
        if len(nums) < 2:
            return len(nums)
        i = 2
        while i < len(nums):
            if nums[i] == nums[i - 2]:
                del nums[i]
            else:
                i += 1
        return len(nums)
