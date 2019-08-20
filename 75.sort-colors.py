#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, head, tail = 0, 0, len(nums) - 1
        while i <= tail:
            while nums[i] == 0 and head <=i or nums[i] == 2 and tail >= i:
                if nums[i] == 0:
                    nums[i], nums[head] = nums[head], nums[i]
                    head += 1
                if nums[i] == 2:
                    nums[i], nums[tail] = nums[tail], nums[i]
                    tail -= 1
            i += 1
