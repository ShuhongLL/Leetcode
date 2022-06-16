import collections

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 初始值为-1
        d1 = collections.defaultdict(lambda: -1)
        d2 = collections.defaultdict(lambda: -1)
        cur, result = 0, 0
        
        for i, char in enumerate(s):
            cur += (i - d1[char]) - (d1[char] - d2[char])
            d2[char] = d1[char]
            d1[char] = i
            result += cur
        return result
