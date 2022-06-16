class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        window_sum = 0
        result = float('inf')
        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target and start <= end:
                result = min(result, end - start + 1)
                window_sum -= nums[start]
                start += 1 
        return 0 if result == float('inf') else result
