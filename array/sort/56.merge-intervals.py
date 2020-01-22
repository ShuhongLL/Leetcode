#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key = lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                start = result[-1][0]
                # note: intervals[i] might be subset of result[-1]
                end = max(intervals[i][1], result[-1][1])
                result.pop(-1)
                result.append([start, end])
            else:
                result.append(intervals[i])
        return result
