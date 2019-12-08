class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0
        # result = 0
        # l, r = 0, 0
        # while r < len(s):
        #     if len(set(map(tuple, s[l:r+1]))) == len(s[l: r+1]):
        #         result = max(result, len(s[l: r+1]))
        #         r += 1
        #     else:
        #         l += 1
        # return result

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
