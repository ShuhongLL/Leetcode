#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
import collections

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = collections.Counter(secret)
        g = collections.Counter(guess)
        bulls = sum(1 for i in range(len(secret)) if secret[i] == guess[i])
        cows = sum(min(s[key], g[key]) for key in s if key in g)
        # same as:
        # for key in s:
        #     if key in g:
        #         cows += (min(s[key], g[key]))
        return f'{bulls}A{cows-bulls}B'

# @lc code=end

