#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.result = []
        self.back_tracking(nums, [])
        return self.result
        
    def back_tracking(self, nums: List[int], path: str):
        if not nums:
            self.result.append(path)
            return
        for i in range(len(nums)):
            self.back_tracking(nums[:i] + nums[i+1:len(nums)], path + [nums[i]])

# del list[index] will apply directly on the object, thus need copy the orignal list:
# copy: new_list = old_list.copy()
# slice: new_list = old_list[:]
# list: new_list = list(old_list)
