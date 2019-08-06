#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            result[tuple(sorted(s))].append(s)
        return result.items
        