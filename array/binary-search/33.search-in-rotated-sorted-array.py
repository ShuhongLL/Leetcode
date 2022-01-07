#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        
        # edge case
        if nums[l] == target:   return l
        if nums[r] == target:   return r

        while l < r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            else:
                if nums[r] < target or nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
        return -1
