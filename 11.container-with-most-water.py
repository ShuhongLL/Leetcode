#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        print(j)
        maxVal = 0
        for _ in range(len(height)):
            if i == j:
                break
            width = abs(i - j)
            maxVal = max(maxVal, width * min(height[i], height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return maxVal
