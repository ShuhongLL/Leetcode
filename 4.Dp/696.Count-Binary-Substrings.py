class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 0011 有两个count
        # 对连续的0/1进行分组
        result = 0
        cur, prev = 1, 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                result += min(cur, prev)
                cur, prev = 1, cur
            else:
                cur += 1
        return result + min(cur, prev)
