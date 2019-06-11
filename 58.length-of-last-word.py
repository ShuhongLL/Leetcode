#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        if s.rfind(' ') != -1:
            return len(s) - s.rfind(' ') - 1
        return len(s)
        
