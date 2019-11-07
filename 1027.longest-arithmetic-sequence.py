#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Sequence
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = {}
        for i, num2 in enumerate(A[1:], start=1):
            for j, num1 in enumerate(A[:i]):
                d = num2 - num1
                if (j, d) in memo:
                    memo[i, d] = memo[j, d] + 1
                else:
                    memo[i, d] = 2
        return max(memo.values())
        
# @lc code=end

