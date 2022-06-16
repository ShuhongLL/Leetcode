#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # edge
        if not matrix or not matrix[0]:
            return False
        
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                if target in matrix[i]:
                    return True
                else:
                    return False
        return False

