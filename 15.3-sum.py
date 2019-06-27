#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for key in range(len(nums)):
            dictMap = {}
            for ite in range(key + 1, len(nums)):
                if nums[ite] in dictMap:
                    tmp = [nums[key], nums[dictMap[nums[ite]]], nums[ite]]
                    tmp.sort()
                    if not tmp in result:
                        result.append(tmp)
                else:
                    dictMap[-nums[key] - nums[ite]] = ite
        return result
