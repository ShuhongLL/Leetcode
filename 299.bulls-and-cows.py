#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        seen = []
        for i in range(len(secret)):
            if guess[i] in secret and guess[i] not in seen:
                cows += min(secret.count(guess[i]), guess.count(guess[i]))
                seen.append(guess[i])
            if guess[i] == secret[i]:   bulls += 1
        return f'{bulls}A{cows-bulls}B'

# @lc code=end

