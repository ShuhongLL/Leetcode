class Solution:
    def numDecodings(self, s: str) -> int:
        if s [0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        # dp[0]  dp[1]   dp[2]  ...
        #         s[0]   s[1]   ...
        for i in range(1, len(s)):
            # a  b(cur)  where a = 0
            # 0b only valid as _0, b
            if s[i-1] == '0':
                # if b = 0 then -> 00 as invalid
                if s[i] == '0':
                    return 0
                dp[i+1] += dp[i]
            # a  b(cur)  where a != 0
            else:
                num = int(s[i-1: i+1])
                if num <= 26:
                    dp[i+1] += dp[i-1]
                # a  b(cur)  where b != 0
                if s[i] != '0':
                    dp[i+1] += dp[i]
        return dp[-1]
