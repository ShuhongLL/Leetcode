#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(2**n):
            result.append(i ^ (i >> 1))
        return result
# @lc code=end

