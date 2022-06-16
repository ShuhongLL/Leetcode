#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        result = sorted(count.items(), key = lambda x: -x[1])
        return [result[i][0] for i in range(k)]

# @lc code=end

