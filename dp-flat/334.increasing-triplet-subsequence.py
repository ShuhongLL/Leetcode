class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        firstMin = nums[0]
        secondMin = float('inf')
        for i in range(1, len(nums)):
            # has to be <= not <
            # to avoid assign duplicate value to secondMin
            if nums[i] <= firstMin:
                firstMin = nums[i]
            elif nums[i] < secondMin:
                secondMin = nums[i]
            elif nums[i] > secondMin:
                return True
        return False
