#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dicts = {}
        for i, ch in enumerate(order):
            dicts[ch] = i
        for i in range(len(words) - 1):
            l = words[i]
            r = words[i+1]
            while l and r:
                if dicts[l[0]] > dicts[r[0]]:
                    return False
                if dicts[l[0]] < dicts[r[0]]:
                    break
                l = l[1:]
                r = r[1:]
            if len(l) != 0 and len(r) == 0:
                return False
        return True   
# @lc code=end

