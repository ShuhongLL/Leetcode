#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from the tail

        # edge
        if not nums:
            return False
        if len(nums) == 1:
            return True
        last = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last == 0
