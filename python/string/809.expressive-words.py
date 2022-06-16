#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#

# @lc code=start
import itertools
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        count = 0
        target = [(key, len(list(group))) for key, group in itertools.groupby(S)]
        for query in words:
            chars = [(key, len(list(group))) for key, group in itertools.groupby(query)]
            if len(target) != len(chars):
                continue
            for i in range(len(target)):
                c1, l1 = chars[i]
                c2, l2 = target[i]
                if c1 != c2:    break
                if (l1 < l2 and l2 < 3) or l1 > l2: break
            else:    count += 1   
        return count
  
# @lc code=end

