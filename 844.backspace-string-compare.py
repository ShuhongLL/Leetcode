#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        p1, d1 = len(S) - 1, 0
        p2, d2 = len(T) - 1, 0
        
        s, t = '', ''
        while p1 >= 0:
            if S[p1] == '#':
                p1, d1 = p1-1, d1+1
            else:
                if d1 > 0:
                    p1, d1 = p1-1, d1-1
                else:
                    s = S[p1] + s
                    p1 -= 1

        while p2 >= 0:
            if T[p2] == '#':
                p2, d2 = p2-1, d2+1
            else:
                if d2 > 0:
                    p2, d2 = p2-1, d2-1
                else:
                    t = T[p2] + t
                    p2 -= 1
        return s == t
        
# @lc code=end

