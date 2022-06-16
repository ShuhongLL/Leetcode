class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) == 0 or len(t) == 0:
            return len(t) == 1 or len(s) == 1
        p1, p2 = 0, 0
        len1, len2 = len(s), len(t)
        while p1 < len1 and p2 < len2:
            if s[p1] != t[p2]:
                return s[p1+1:] == t[p2+1:] or s[p1+1:] == t[p2:] or s[p1:] == t[p2+1:]
            p1 += 1
            p2 += 1
        return (p1 == len1 and p2 == len2-1) or (p2 == len2 and p1 == len1-1)
