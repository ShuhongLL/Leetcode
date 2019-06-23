#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        backMax = s[0]
        curMax = maxStr = 1
        for i in range(1, len(s)):
            while s[i] in backMax and len(backMax) != 0:
                backMax = backMax[1:]
            backMax = backMax + s[i]
            
            curMax = max(curMax, len(backMax))
            maxStr = max(maxStr, curMax)
        return maxStr
