#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
class Solution:
    def numTrees(self, n: int) -> int:
        self.dicts = {}
        return self.dp(n)

    def dp(self, n: int) -> int:
        if n <= 1:
            return 1
        if n in self.dicts:
            return self.dicts[n]
        result = 0
        for i in range(n):
            result += self.dp(i) * self.dp(n - (i + 1))
        self.dicts[n] = result
        return result
