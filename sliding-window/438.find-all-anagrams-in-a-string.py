#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        result = []
        cur_sum, tar_sum = 0, 0
        for i in range(len(p)):
            cur_sum += hash(s[i])
            tar_sum += hash(p[i])
        if cur_sum == tar_sum:
            result.append(0)
        prev = 0
        for i in range(len(p), len(s)):
            cur_sum += (hash(s[i]) - hash(s[prev]))
            prev += 1
            if cur_sum == tar_sum:
                result.append(prev)
        return result

# @lc code=end

