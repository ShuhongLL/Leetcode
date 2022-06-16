#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # edge
        if n == 1:
            return [[1]]

        result = []
        def recursiveFind(nums: List[int], remain: int, path: List[int]):
            if remain == 0:
                result.append(path)
                return
            for i in range(len(nums) - remain + 1):
                if nums[i] in path:
                    continue
                recursiveFind(nums[i:], remain - 1, path + [nums[i]])
        recursiveFind([i for i in range(1, n + 1)], k, [])
        return result
