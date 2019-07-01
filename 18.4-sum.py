#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find_n_sum(nums, N, path, results, target):
            if len(nums) < N or N < 2 or (nums[0] * N > target or nums[-1] * N < target):
                return []
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        results.append(path + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        find_n_sum(nums[i + 1:], N - 1, path + [nums[i]], results, target - nums[i])
                        
        path, results = [], []
        find_n_sum(sorted(nums), 4, path, results, target)
        return results
