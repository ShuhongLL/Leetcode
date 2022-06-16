#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        uniqueNums = list(set(nums))
        return target in uniqueNums
