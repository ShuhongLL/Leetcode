import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        # len, start, end
        result = (float('inf'), 0, 0)
        l, r = 0, 0
        t_dicts = collections.Counter(t)
        required = len(t_dicts)
        
        cur_window = collections.defaultdict(int)
        formed = 0

        while r < len(s):
            char = s[r]
            cur_window[char] += 1
            if char in t_dicts and cur_window[char] == t_dicts[char]:
                formed += 1
                
            while l <= r and formed == required:
                toDel = s[l]
                if r-l+1 < result[0]:
                    result = (r-l+1, l, r)
                cur_window[toDel] -= 1
                if toDel in t_dicts and cur_window[toDel] < t_dicts[toDel]:
                    formed -= 1
                l += 1
            r += 1
 
        return "" if result[0] == float('inf') else s[result[1]: result[2]+1]
