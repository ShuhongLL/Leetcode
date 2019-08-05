#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        int_s = sorted(intervals)

        for i in range(0, len(int_s)):
            if results:
                l = len(results) - 1
                if results[l][1] >= int_s[i][0]:
                    results[l][1] = max(results[l][1], int_s[i][1])
                else:
                    results.append(int_s[i])
            else:
                results.append(int_s[i])

        return results
