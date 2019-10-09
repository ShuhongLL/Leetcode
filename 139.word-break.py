#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        self.dicts = wordDict
        return self.divideAndConquer(s)

    def divideAndConquer(self, s: str) -> bool:
        if not s or s in self.dicts:
            self.memo[s] = True
            return True
        for i in range(1, len(s)):
            l, r = s[:i], s[i:]
            if r in self.memo:
                if self.memo[r]:
                    return True
                continue
            if l in self.dicts:
                if self.divideAndConquer(r):
                    self.memo[r] = True
                    return True
                self.memo[r] = False
        return False
# @lc code=end

