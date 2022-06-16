#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = self.merge_sort(nums)
        if result[0] == 0:
            return '0'
        return ''.join(str(i) for i in result)

    def merge_sort(self, nums: List[int]):
        if not nums or len(nums) == 1:
            return nums
        mid = len(nums) // 2
        l = self.merge_sort(nums[:mid])
        r = self.merge_sort(nums[mid:])
        # merge
        result = []
        while l and r:
            if self.l_grt_r(str(l[0]), str(r[0])):
                result += [l[0]]
                del l[0]
            else:
                result += [r[0]]
                del r[0]
        if l:
            result += l
        else:
            result += r
        return result
    
    def l_grt_r(self, l: str, r: str):
        num1 = int(l + r)
        num2 = int(r + l)
        return num1 > num2

# @lc code=end
