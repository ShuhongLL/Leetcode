#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = collections.defaultdict(lambda: 0)
        sum_dict[0] = 1
        sums, result = 0, 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums - k in sum_dict:
                result += sum_dict[sums - k]
            sum_dict[sums] += 1
        return result

# @lc code=end

