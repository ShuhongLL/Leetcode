#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        low = 0
        high = x
        quess = math.floor((low + high) / 2)
        while not (quess**2 <= x and (quess + 1)**2 > x):
            if quess**2 < x:
                low = quess
            else:
                high = quess
            quess = math.floor((low + high) / 2)
        return quess

