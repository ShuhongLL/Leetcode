#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                del nums[index]
                index -= 1
            index += 1
        return len(nums)
