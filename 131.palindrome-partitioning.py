#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.memo = {}
        return self.divideAndConqur(s)

    def divideAndConqur(self, s: str):
        if not s:
            return []
        if len(s) == 1:
            return [[s]]
        if s in self.memo:
            return self.memo[s]
        answer = []
        for i in range(1, len(s)):
            l, r = s[:i], s[i:]
            if l == l[::-1]:
                for subset in self.divideAndConqur(r):
                    answer.append([l] + subset)
        if s == s[::-1]:
            answer.append([s])
        return answer

# @lc code=end

