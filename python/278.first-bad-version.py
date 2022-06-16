#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, end: int, start: int = 0):
        """
        :type n: int
        :rtype: int
        """
        if end == start:
            return start
        if end == start + 1:
            return start if isBadVersion(start) else end
        mid = (end - start) // 2 + start
        if isBadVersion(mid):
            return self.firstBadVersion(mid, start)
        else:
            return self.firstBadVersion(end, mid+1)

        
# @lc code=end

