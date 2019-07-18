#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def recursiceSum(nums: List[int], curTarget: int, path: List[int]):
            if len(nums) != 0:
                if nums[-1] > curTarget:
                    recursiceSum(nums[:-1], curTarget, path)
                elif nums[-1] == curTarget:
                    result.append(path + [nums[-1]])
                    recursiceSum(nums[:-1], curTarget, path)
                else:
                    recursiceSum(nums, curTarget - nums[-1], path + [nums[-1]])
                    recursiceSum(nums[:-1], curTarget, path)
                    
        recursiceSum(candidates, target, [])
        return result

