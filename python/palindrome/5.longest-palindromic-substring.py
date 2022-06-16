#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s 
        cur = maxStr = s[0]
        for i in range(1, len(s)):
            cur = s[:i+1]
            while cur[::-1] != cur:
                cur = cur[1:]
            maxStr = cur if len(cur) > len(maxStr) else maxStr
        return maxStr
