#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        # sort list: O(nlgn)
        nums_s = sorted(nums)
        result = []

        def recursiveFindPermutation(nums: List[int], index: int, path: List[int]):
            nums_c = nums[:]
            if index >= 0:
                del nums_c[index]
            if len(nums_c) != 0:
                p_i = 0
                for i in range(len(nums_c)):
                    if nums_c[i] == nums_c[p_i] and i != 0:
                        continue
                    p_i = i
                    recursiveFindPermutation(nums_c, i, path + [nums_c[i]])
            else:
                result.append(path)

        recursiveFindPermutation(nums_s, -1, [])
        return result
