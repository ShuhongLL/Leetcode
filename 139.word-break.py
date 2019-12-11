#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    # method 1: divide and conquer + memorization
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     self.memo = {}
    #     self.dicts = wordDict
    #     return self.divideAndConquer(s)

    # def divideAndConquer(self, s: str) -> bool:
    #     if not s or s in self.dicts:
    #         self.memo[s] = True
    #         return True
    #     for i in range(1, len(s)):
    #         l, r = s[:i], s[i:]
    #         if r in self.memo:
    #             if self.memo[r]:
    #                 return True
    #             continue
    #         if l in self.dicts:
    #             if self.divideAndConquer(r):
    #                 self.memo[r] = True
    #                 return True
    #             self.memo[r] = False
    #     return False

    # method 2: dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # record each time the current index can be constructed by the dict
        # refer to the previous valid index, check if s[prevs, cur] is in the dict
        # if so, update memo by appending the cur index
        # next time, cur will be one of the prevs
        memo = [0]
        for i in range(len(s)+1):
            for index in memo[::-1]:
                if s[index:i] in wordDict:
                    memo.append(i)
                    break
        return len(s) in memo

# @lc code=end

