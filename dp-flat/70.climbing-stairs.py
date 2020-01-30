#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        s = [0] * (n + 1)
        s[0] = 1
        s[1] = 1
        for i in range(2, n+1):
            s[i] = s[i-1] + s[i-2]
        return s[-1]
