#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        tar = len(nums) - 2
        while tar >= 0 and nums[tar] >= nums[tar+1]:
            tar -= 1
        if tar == -1:
            nums.sort()
            return
        
        swap = len(nums) - 1
        while tar < swap and nums[swap] <= nums[tar]:
            swap -= 1
        nums[tar], nums[tar+1:len(nums)] = nums[swap], sorted(nums[tar:swap] + nums[swap+1:len(nums)])

