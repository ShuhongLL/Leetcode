#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        while nums1 and nums2:
            if nums1[0] == nums2[0]:
                result.append(nums1[0])
                nums1.pop(0)
                nums2.pop(0)
            elif nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
        return result

# @lc code=end

