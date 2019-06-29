#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # edge
        if len(nums) <= 3:
            return sum(nums)
        
        # sort list: O(nlgn)
        nums_s = sorted(nums)

        if target <=sum(nums_s[:3]):
            return sum(nums_s[:3])
        elif target >=sum(nums_s[-3:]):
            return sum(nums_s[-3:])
        else:
            closest = 0
            minDif = abs(sum(nums_s[:3]) - target)
            # p stands for pivot
            # p_i stands for pivot index
            # p_v stands for pivot value
            for p_i in range(len(nums_s) - 2):
                p_v = nums_s[p_i]
                # skip if the pivot is the same
                if p_i != 0 and p_v == nums_s[p_i - 1]:
                    continue
                # p_h stands for the head
                # p_t stands fot the tail
                p_h = p_i + 1
                p_t = len(nums_s) - 1
                while p_h < p_t:
                    threeSum = p_v + nums_s[p_h] + nums_s[p_t]
                    dif = abs(threeSum - target)
                    if dif < minDif:
                        minDif = dif
                        closest = threeSum
                    if threeSum > target:
                        p_t -= 1
                    elif threeSum < target:
                        p_h += 1
                    else:
                        return threeSum
        return closest
