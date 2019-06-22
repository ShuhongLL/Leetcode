#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        while n - 2 > 0:
            third = first + second
            first = second
            second = third
            n -= 1
        return second
        