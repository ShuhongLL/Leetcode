class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(0, len(haystack) - len(needle) + 1):
            p1, p2 = i, 0
            while haystack[p1] == needle[p2]:
                if p2 == len(needle)-1:
                    return i
                p1 += 1
                p2 += 1
        return -1
