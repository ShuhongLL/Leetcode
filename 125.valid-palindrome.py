#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r'[\w]+', s)).lower()
        return s == s[::-1]
        
# @lc code=end

