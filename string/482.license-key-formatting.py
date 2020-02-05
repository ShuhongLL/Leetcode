#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.replace('-', '').upper()
        rem = len(s) % K
        head_str = s[:rem]
        tail_str = s[rem:]
        tail_str = '-'.join([tail_str[i:i+K] for i in range(0, len(tail_str), K)])
        if head_str and tail_str:
            return f'{head_str}-{tail_str}'
        return head_str + tail_str
# @lc code=end

