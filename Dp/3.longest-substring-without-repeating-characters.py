class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        start = 0
        memo = {}
        for end in range(len(s)):
            if s[end] in memo:
                start = max(start, memo[s[end]])
            result = max(result, end - start + 1)
            memo[s[end]] = end + 1 # last non-repeating index
        return result
