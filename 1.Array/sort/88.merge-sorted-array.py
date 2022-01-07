#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[len(nums1) - n:] = nums2
        # return nums1.sort()
        if not nums2:
            return
        nums1[len(nums1) - m:] = nums1[:m]
        p, p1, p2 = 0, len(nums1)-m, 0
        while p1 < len(nums1) and p2 < n:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
        if p2 < n:
            nums1[-(n-p2):] = nums2[p2:]

# @lc code=end
