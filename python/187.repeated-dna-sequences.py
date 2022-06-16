#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = { s[:10]: 1 }
        result = set()
        prev = s[:10]
        for i in s[10:]:
            new = prev[1:] + i
            if new in seen:
                result.add(new)
            seen[new] = 1
            prev = new
        return list(result)
# @lc code=end

