class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        1结尾：单增，无需翻转
        0结尾：0需要翻转为1，或保持0翻转之前所有1
        """
        countOne = 0
        dp = [0 for _ in range(len(s) + 1)]
        for i in range(len(s)):
            if s[i] == "1":
                dp[i+1] = dp[i]
                countOne += 1
            else:
                dp[i+1] = min(1 + dp[i], countOne)
        return dp[-1]
