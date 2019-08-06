#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n = n >> 1
        return result
