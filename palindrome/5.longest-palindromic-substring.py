class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            cur = s[:i+1]
            while cur != cur[::-1]:
                cur = cur[1:]
            result = cur if len(cur) > len(result) else result 
        return result