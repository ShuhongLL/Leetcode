# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         memo = {}
#         for i in range(len(s)):
#             memo[i, i] = 1
#         for l in range(1, len(s)):
#             for head in range(0, len(s)-l):
#                 tail = head + l
#                 if s[head] == s[tail]:
#                     if head + 1 != tail:
#                         memo[head, tail] = memo[head+1, tail-1] + 2
#                     else:
#                         memo[head, tail] = 2
#                 else:
#                     memo[head, tail] = max(memo[head+1, tail], memo[head, tail-1])
#         return memo[0, len(s)-1]

from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 1
            elif i > j:
                return 0
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)
            else:
                return max(dp(i + 1, j), dp(i, j - 1))
        return dp(0, len(s) - 1)
