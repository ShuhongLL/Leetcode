#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        result = []
        size = len(p)
        target_sum = 0
        # sum up the target hash value
        for letter in p:
            target_sum += hash(letter)
        # sum up hash value of the first len(p) in s
        cur_sum = 0
        for i in range(size):
            cur_sum += hash(s[i])
        if cur_sum == target_sum:
            result.append(0)
        # start from index len(p), compare target and cur
        cur = 0
        for i in range(size, len(s)):
            cur_sum += (hash(s[i]) - hash(s[cur]))
            cur += 1
            if cur_sum == target_sum:
                result.append(cur)
        return result
        
# @lc code=end

