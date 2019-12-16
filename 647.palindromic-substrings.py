class Solution:
    def countSubstrings(self, s: str) -> int:
        # memo-ization + dp
        if not s:
            return 0
        memo = {}
        size = len(s)
        result = size

        for l in range(1, size):
            for start in range(0, size - l):
                end = start + l
                if start + 1 == end:
                    memo[start, end] = s[start] == s[end]
                else:
                    memo[start, end] = s[start] == s[end] and (start+1 == end-1 or memo[start+1, end-1])
                if memo[start, end]:
                    result += 1
        return result
