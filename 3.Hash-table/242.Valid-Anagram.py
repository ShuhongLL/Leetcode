from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        memo = [0] * 26
        for i in range(len(s)):
            # 相对位置
            memo[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            memo[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if memo[i] != 0:
                return False
        return True
    
        # return Counter(s) == Counter(t)
