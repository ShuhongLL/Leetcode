#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.replace('-', '').upper()
        head = len(s) % K
        head_result = s[:head]
        tail_str = s[head:]
        chunk, chunk_size = len(tail_str), K
        tail_result = '-'.join([tail_str[i:i+chunk_size] for i in range(0, chunk, chunk_size)])
        if len(head_result) != 0 and len(tail_result) != 0:
            return f'{head_result}-{tail_result}'
        return head_result + tail_result

# @lc code=end

