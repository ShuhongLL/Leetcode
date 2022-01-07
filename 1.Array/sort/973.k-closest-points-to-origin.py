#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []
        length = []
        for num in points:
            length.append([num[0]*num[0] + num[1]*num[1], num])
        length = sorted(length)
        return [length[i][1] for i in range(K)]

# @lc code=end

