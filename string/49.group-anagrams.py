#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = collections.defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            memo[key].append(s)
        return [memo[key] for key in memo]
