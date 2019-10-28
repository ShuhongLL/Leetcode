#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        monotone_increasing = not any(A[i] > A[i+1] for i in range(len(A) - 1))
        monotone_decreasing = not any(A[i] < A[i+1] for i in range(len(A) - 1))
        return monotone_increasing or monotone_decreasing
        
# @lc code=end

