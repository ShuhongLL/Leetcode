#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            return sum(nums)
        nums = sorted(nums)

        if target <=sum(nums[:3]):
            return sum(nums[:3])
        elif target >=sum(nums[-3:]):
            return sum(nums[-3:])
        result = 0
        minDif = abs(sum(nums[:3]) - target)
        for i in range(len(nums) - 2):
            v = nums[i]
            # skip if the pivot is the same
            if i > 0 and v == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            # two pointers
            while l < r:
                cur = v + nums[l] + nums[r]
                dif = abs(cur - target)
                if dif < minDif:
                    minDif = dif
                    result = cur
                if cur > target:
                    r -= 1
                elif cur < target:
                    l += 1
                else:
                    return cur
        return result
