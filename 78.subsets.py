#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # edge
        if not nums:
            return []
        result = []
        def recursiveFind(nums: List[int], path: List[int]):
            result.append(path)
            for i in range(len(nums)):
                recursiveFind(nums[i + 1:], path + [nums[i]])
        recursiveFind(nums, [])
        return result

