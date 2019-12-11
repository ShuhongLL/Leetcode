class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] = max(nums[i-2], nums[i-3]) + nums[i]
        return max(nums[-1], nums[-2])
