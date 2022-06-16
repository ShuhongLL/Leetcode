#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
import itertools

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort list: O(nlgn)
        nums_s = sorted(candidates)
        result = []
        def recursiveSum(nums: List[int], curTarget: int, path: List[int]):
            if len(nums) != 0:
                if nums[-1] > curTarget:
                    recursiveSum(nums[:-1], curTarget, path)
                elif nums[-1] == curTarget:
                    result.append(path + [nums[-1]])
                    recursiveSum(nums[:-1], curTarget, path)
                else:
                    recursiveSum(nums[:-1], curTarget - nums[-1], path + [nums[-1]])
                    recursiveSum(nums[:-1], curTarget, path)
        recursiveSum(nums_s, target, [])
        return [k for k, _ in itertools.groupby(sorted(result))]
