#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]], pre_fresh: int = 0, mins: int = 0) -> int:
        nums = copy.deepcopy(grid)
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    if i > 0 and grid[i-1][j] == 1:
                        nums[i-1][j] = 2
                    if j > 0 and grid[i][j-1] == 1:
                        nums[i][j-1] = 2
                    if i < len(grid)-1 and grid[i+1][j] == 1:
                        nums[i+1][j] = 2
                    if j < len(grid[0])-1 and grid[i][j+1] == 1:
                        nums[i][j+1] = 2
                if grid[i][j] == 1:
                    fresh += 1
        if pre_fresh == fresh:
            return 0 if fresh == 0 else -1
        if fresh > 0:
            return self.orangesRotting(nums, fresh, mins + 1)
        return mins

# @lc code=end

