#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # edge
        if len(nums) < 3:
            return []
        
        # sort input list: O(nlgn)
        nums_s = sorted(nums)
        result = set()

        # p:    pivot
        # p_i:  pivot index
        # p_v:  pivot value
        for p_i in range(len(nums_s) - 2):
            p_v = nums_s[p_i]

            # since the sum need to be zero and the list is sorted
            # no need to check pivot greater than zero
            if p_v <= 0:
                # no need check the same pivot once again
                if p_v > nums_s[p_i - 1] or p_i == 0:
                    dictMap = {}
                    for i in nums_s[p_i + 1 :]:
                        # same as two sum
                        if i not in dictMap:
                            # no need to record the third value
                            dictMap[-p_v - i] = 1
                        else:
                            result.add((p_v, i, -p_v - i))
        return list(result)
