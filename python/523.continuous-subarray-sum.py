#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if k == 0:
            return any(nums[i] + nums[i+1] == 0 for i in range(len(nums)-1))
        sums = 0
        dicts = {0: -1}
        for i in range(len(nums)):
            sums += nums[i]
            mod = sums % k
            if mod in dicts and i - dicts[mod] > 1:
                return True
            if mod not in dicts:
                dicts[mod] = i
        return False

# @lc code=end

