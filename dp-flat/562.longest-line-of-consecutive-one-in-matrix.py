class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        result = 0
        dp = [[[0, 0, 0, 0] for _ in range(len(M[0]))] for _ in range(len(M))]
        for row in range(len(M)):
            for col in range(len(M[0])):
                if M[row][col] == 0:
                    continue
                # vertical count
                if row == 0:
                    dp[row][col][1] = M[row][col]
                else:
                    dp[row][col][1] = dp[row-1][col][1] + 1
                # horizontal count
                if col == 0:
                    dp[row][col][0] = M[row][col]
                else:
                    dp[row][col][0] = dp[row][col-1][0] + 1
                # diagonal count
                if row != 0 and col != 0:
                    dp[row][col][2] = dp[row-1][col-1][2] + 1
                else:
                    dp[row][col][2] = M[row][col]
                # anti-diagonal count
                if row != 0 and col != len(M[0]) - 1:
                    dp[row][col][3] = dp[row-1][col+1][3] + 1
                else:
                    dp[row][col][3] = M[row][col]
                # update max result
                result = max(dp[row][col] + [result])
        return result
