#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s 
        curMax = maxStr = s[0]
        for i in range(1, len(s)):
            curMax = s[:i+1]
            while curMax[::-1] != curMax:
                curMax = curMax[1:]
            maxStr = curMax if len(curMax) > len(maxStr) else maxStr
        return maxStr
