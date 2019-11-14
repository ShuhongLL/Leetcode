#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#

# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        q = [self.f(query) for query in queries]
        w = [self.f(word) for word in words]
        result = []
        for query in q:
            count = sum(1 for word in w if word > query)
            result.append(count)
        return result
    
    def f(self, s: str):
        ss = sorted(s)
        return sum(1 for v in ss if v == ss[0])

# @lc code=end

