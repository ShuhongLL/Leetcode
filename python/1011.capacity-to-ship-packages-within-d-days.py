#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            days, cur_sum = 1, 0
            mid = (l + r) // 2
            for weight in weights:
                if cur_sum + weight > mid:
                    cur_sum = weight
                    days += 1
                else:
                    cur_sum += weight
            if days <= D:
                r = mid
            else:
                l = mid + 1
        return r
        # or return l, same
# @lc code=end

