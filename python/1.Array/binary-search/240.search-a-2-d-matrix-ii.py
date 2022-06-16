#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                return False
            if matrix[i][-1] >= target:
                if self.binary_serach(matrix[i], target):
                    return True
        return False
                
    def binary_serach(self, row: List[int], target: int):
        l, r = 0, len(row) - 1
        while l < r:
            mid = (l + r)//2
            if row[mid] == target:
                return True
            if row[mid] > target:
                r = mid
            else:
                l = mid + 1
        # note: l might equal to r
        # e.g [1]
        return row[l] == target

# @lc code=end

