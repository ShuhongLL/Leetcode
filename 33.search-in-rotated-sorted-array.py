#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int, index:int = 0) -> int:
        # edge
        if not nums:
            return -1
        l = 0
        r = len(nums)-1
        if nums[l] == target:   return l
        elif nums[r] == target:   return r

        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[r]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid
                else:
                    r = mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid
                else:
                    l = mid
        return -1
