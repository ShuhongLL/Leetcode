import collections

class Solution:
    # same as flipping the coin
    #   prev: the previous max value
    # keep track of used & not_used:
    #   take the previous max
    #   not take previous max
    def deleteAndEarn(self, nums: List[int]) -> int:
        prev = -1
        used, not_used = 0, 0
        count = collections.Counter(nums)
        for key in sorted(count):
            if key != prev + 1:
                used, not_used = max(used, not_used) + count[key] * key, max(used, not_used)
            else:
                used, not_used = not_used + count[key] * key, max(used, not_used)
            prev = key
        return max(used, not_used)
