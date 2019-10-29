#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        if not A or not B:
            return result
        while A and B:
            _max = max(A[0][0], B[0][0])
            _min = min(A[0][1], B[0][1])
            if _max <= _min:
                result.append([_max, _min])
            if A[0][1] < B[0][1]:
                A.pop(0)
            else:
                B.pop(0)
        return result
        
# @lc code=end

