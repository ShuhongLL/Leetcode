#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
#     Memory limit exceed...
#     def longestCommonSubsequence(self, text1: str, text2: str, count: int = 0) -> int:
#         self.seen = {}
#         return self.lcs(text1, text2)
        
#     def lcs(self, t1: str, t2: str):
#         if not t1 or not t2:
#             return 0
#         if (t1, t2) in self.seen:
#             return self.seen[t1, t2]
#         r1 = self.lcs(t1[1:], t2[1:]) + 1 if t1[0] == t2[0] else 0
#         r2 = self.lcs(t1[1:], t2)
#         r3 = self.lcs(t1, t2[1:])
#         r = max(r1, r2, r3)
#         self.seen[t1, t2] = r
#         return r

    def longestCommonSubsequence(self, text1: str, text2: str, count: int = 0) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if text1[i-1] != text2[j-1] else dp[i-1][j-1] + 1
        return dp[-1][-1]

# @lc code=end

