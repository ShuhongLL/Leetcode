class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        maxTotal = 0

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if x == 0 or y == 0:
                    dp[x][y] = int(matrix[x][y])
                elif matrix[x][y] == "1":
                    dp[x][y] = min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + 1
                maxTotal = max(maxTotal, dp[x][y])
        print(dp)
        return maxTotal ** 2
