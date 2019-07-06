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
        # p_i stands for the index of the current pivot  
        # t_i stands for the index of the target pivot to be swapped
        if len(nums) > 1:
            p_i = len(nums) - 1
            while p_i != 0 and (p_i == len(nums) - 1 or nums[p_i] >= nums[p_i + 1]):
                p_i -= 1
            if p_i == 0 and nums[0] >= nums[1]:
                # numpy: nums.sort()
                nums[:] = sorted(nums[:])
                return None
            t_i = p_i
            p_i += 1
            while p_i <= len(nums) - 1:
                if nums[p_i] <= nums[t_i]:
                    break
                # when p_i == len(nums) - 1, plus one here first then minors afterwards to swap
                p_i += 1
            nums[p_i - 1], nums[t_i] = nums[t_i], nums[p_i - 1]
            # numpy: nums[t_i + 1:].sort()
            nums[t_i + 1:] = sorted(nums[t_i + 1:])
