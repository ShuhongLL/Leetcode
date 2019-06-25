#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = ['' for x in range(numRows)]
        for i in range(len(s)):
            re = i % (2 * numRows - 2)
            if re > numRows - 1:
                re = (2 * numRows - 2) - re
            arr[re] += s[i]
        return ''.join(e for e in arr)
