class Solution:
    def countArrangement(self, N: int) -> int:
        nums = [i for i in range(1, N+1)]
        self.result = 0
        self.back_track(nums, 1)
        return self.result
        
    def back_track(self, nums: List[int], index: int):
        if not nums:
            self.result += 1
            return
        for i in range(len(nums)):
            if nums[i] % index == 0 or index % nums[i] == 0:
                nums_c = nums[:]
                nums_c.pop(i)
                self.back_track(nums_c, index+1)
