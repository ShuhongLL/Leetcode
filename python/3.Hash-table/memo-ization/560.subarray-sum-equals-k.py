#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = collections.defaultdict(lambda: 0)
        memo[0] = 1
        
        cur_sum, result = 0, 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in memo:
                result += memo[cur_sum - k]
            memo[cur_sum] += 1
        return result
