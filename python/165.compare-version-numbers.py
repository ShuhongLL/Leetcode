#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        str1 = version1.split('.')
        str2 = version2.split('.')

        length = min(len(str1), len(str2))
        for _ in range(length):
            num1 = int(str1[0])
            num2 = int(str2[0])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            del str1[0]
            del str2[0]
        sum1, sum2 = 0, 0
        for i in str1:
            sum1 += int(i)
        for i in str2:
            sum2 += int(i)
        if sum1 > 0:
            return 1
        if sum2 > 0:
            return -1
        return 0

# @lc code=end

