#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) <= 1:
            return [nums]

        def recursiveFindPermutation(nums: List[int], index: int, path: List[int]) -> None:
            nums_c = nums[:]
            if index >= 0:
                del nums_c[index]
            if len(nums_c) != 0:
                for i in range(len(nums_c)):
                    recursiveFindPermutation(nums_c, i, path + [nums_c[i]])
            else:
                result.append(path)

        recursiveFindPermutation(nums, -1, [])
        return result

# del list[index] will apply directly on the object, thus need copy the orignal list:
# copy: new_list = old_list.copy()
# slice: new_list = old_list[:]
# list: new_list = list(old_list)
