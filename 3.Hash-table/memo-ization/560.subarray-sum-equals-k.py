#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # k = sum(nums[:b]) - sum(nums[:a]), where a< b
        seen = collections.defaultdict(lambda: 0)
        # note: nums[:a] can be empty list []
        seen[0] = 1
        cur_sum, result = 0, 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in seen:
                # seen[cur_sum - k] stores the number of different start points (a)
                result += seen[cur_sum - k]
            # end point (b) moves further
            seen[cur_sum] += 1
        return result

# @lc code=end

