class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        result = 0
        
        for i in range(2):
            if i == 0:
                rstart, rend, rstep = 0, row, 1
                cstart, cend, cstep = 0, col, 1
            else:
                rstart, rend, rstep = row - 1, -1, -1
                cstart, cend, cstep = col - 1, -1, -1
            cmemo = [0] * col
            for m in range(rstart, rend, rstep):
                enemy = 0
                for n in range(cstart, cend, cstep):
                    val = grid[m][n]
                    if val == 'E':
                        enemy += 1
                        cmemo[n] += 1
                    elif val == 'W':
                        enemy = 0
                        cmemo[n] = 0
                    else:
                        cur = int(val) + enemy + cmemo[n]
                        grid[m][n] = str(cur)
                        result = max(result, cur)
        return result
