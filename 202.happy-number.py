#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True
            nums = list(map(int, str(n)))
            n = sum(i**2 for i in nums)
            if n in seen:
                return False
            seen.add(n)

# @lc code=end

