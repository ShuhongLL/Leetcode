#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#

# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        memo = {}
        p = 0
        
        while p < N:
            key = tuple(cells)
            if key in memo:
                cycle = p - memo[key]
                p = p + ((N - p) // cycle) * cycle
                if p == N:
                    return cells
            else:
                memo[key] = p

            tmp = [0] * len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    tmp[i] = 1
            cells = tmp
            p += 1
        return cells

# @lc code=end

