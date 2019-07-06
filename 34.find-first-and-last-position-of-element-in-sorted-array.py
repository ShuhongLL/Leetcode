#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # edge
        if not nums:
            return [-1, -1]
        
        # init start and end pivot
        l = 0
        r = len(nums) - 1
        start = l if nums[l] == target else -1
        end = r if nums[r] == target else -1

        def binarySearch(l: int, r: int, start: int, end: int) -> List[int]:
            if l <= r:
                if nums[l] <= target and nums[r] >= target:
                    mid = (l + r) // 2
                    if nums[mid] < target:
                        return binarySearch(mid + 1, r, start, end)
                    elif nums[mid] > target:
                        return binarySearch(l, mid - 1, start, end)
                    else:
                        l1 = binarySearch(l, mid - 1, start, end)
                        l2 = binarySearch(mid + 1, r, start, end)
                        return [ l1[0] if l1[0] != -1 else mid, l2[1] if l2[1] != -1 else mid  ]     
            return [start, end]
            
        if start != l or end != r:
            return binarySearch(l ,r, start, end)
        else:
            return [start, end]

