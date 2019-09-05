#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
import itertools

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # edge case
        if not nums:
            return []
        self.result = []
        self.recursiveFind(nums, [])
        self.result = sorted(self.result)
        return list(k for k, _ in itertools.groupby(self.result))

    def recursiveFind(self, nums: List[int], path: List[int]):
        self.result.append(sorted(path))
        for i in range(len(nums)):
            self.recursiveFind(nums[i + 1:], path + [nums[i]])
