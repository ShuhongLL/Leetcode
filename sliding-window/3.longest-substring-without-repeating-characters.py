class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        tmp = s[0]
        result = 1
        for i in range(1, len(s)):
            while s[i] in tmp:
                tmp = tmp[1:]
            tmp += s[i]
            result = max(result, len(tmp))
        return result
