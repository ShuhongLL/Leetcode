class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1

        for i in range(1, len(s)):
            v = int(s[i-1: i+1])
            # for [a, b], 10 <= ab <= 26
            if s[i] != '0' and v <= 26 and v >= 10:
                dp[i+1] = dp[i] + dp[i-1]
            # for [a, b], b = 0 and ab <= 26
            elif s[i] == '0' and v <= 26 and v != 0:
                dp[i+1] = dp[i-1]
            # for [a, b], ab > 26
            elif s[i] != '0':
                dp[i+1] = dp[i]
            # invalid
            else:
                return 0
        return dp[-1]
