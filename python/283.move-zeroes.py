class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         j = i
        #         while j < len(nums) and nums[j] == 0:
        #             j += 1
        #         nums[i:] = nums[j:] + [0] * (j-i)
        #     i += 1

        i, t = 0, len(nums)
        while i < t:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                t -= 1
            else:
                i += 1
