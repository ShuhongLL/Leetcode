#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        a = abs(dividend)
        b = abs(divisor)
        result = 0

        while(a - b >= 0):
            x = 0
            while(a - (b << 1 << x) >= 0):
                x += 1
            result += 1 << x
            a -= b << x
        result = result if (dividend > 0) == (divisor > 0) else -result
        if result > 2147483647:
            return 2147483647
        else:
            return result

