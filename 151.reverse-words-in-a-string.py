#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        chars = s.split(' ')
        result = [char.strip() for char in chars if char != '']
        return str.join(' ', result[::-1])
# @lc code=end

