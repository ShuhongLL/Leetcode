#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index <= len(nums) - 1:
            if nums[index] == val:
                del nums[index]
                index -= 1
            index += 1
        return len(nums)
