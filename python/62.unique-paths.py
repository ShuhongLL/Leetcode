#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # edge
        if m == 1 or n == 1:
            return 1

        m -= 1
        n -= 1
        numerator = 1
        denominator = 1
        # swap to use the minimum number to iterate
        if m < n:
            m, n = n, m
        count = m + n
        for _ in range(n):
            numerator *= count
            denominator *= n
            count -= 1
            n -= 1
        
        return numerator // denominator
        