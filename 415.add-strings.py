#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1, num2):
        i, j, carrier, res = len(num1)-1, len(num2)-1, 0, ""
        while i >= 0 or j >=0 or carrier:
            if i >= 0:
                carrier += int(num1[i])
                i -= 1
            if j >= 0:
                carrier += int(num2[j])
                j -= 1
            res += str(carrier % 10)
            carrier //= 10
        return res[::-1]

# @lc code=end

