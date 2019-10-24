#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s or s == s[::-1]:
            return True
        for i in range(len(s) - 1):
            if s[i] != s[-i-1]:
                s1 = s[i+1:-i-1] + s[-i-1]
                s2 = s[i:-i-1]
                return s1 == s1[::-1] or s2 == s2[::-1]
        # should always return in the loop
        # add this extra return for lint
        return True
        
# @lc code=end

