#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
class Solution:
    """
    need iterate twice in case of:
    2 1 1 1 1 1
    1 2 1 1 1 2
    """
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def verify(t: int):
            r1, r2 = 0, 0
            for i in range(len(A)):
                if A[i] != t and B[i] != t: return -1
                if A[i] != t:   r1 += 1
                elif B[i] != t: r2 += 1
            return min(r1, r2)
        result = verify(A[0])
        if A[0] == B[0] or result != -1:
            return result
        else:
            return verify(B[0])

# @lc code=end

