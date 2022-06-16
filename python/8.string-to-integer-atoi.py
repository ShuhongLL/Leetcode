#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

class Solution:
    def myAtoi(self, val: str) -> int:
        val = val.strip()
        if not val:
            return 0
        
        sign = 1
        sumVal = 0
        if val[0] == '-':
            sign = -1
            val = val[1:]
        elif val[0] == '+':
            sign = 1
            val = val[1:]
        for i in range (len(val)):
            if not val[i].isdigit():
                break
            sumVal = sumVal * 10 + int(val[i])
        result = sign * sumVal
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result
