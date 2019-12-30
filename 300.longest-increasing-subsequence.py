class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        result = 1
        for i in range(len(nums)):
            cur = 1
            for n in range(i):
                if nums[n] < nums[i]:
                    cur = max(cur, dp[n] + 1)
            dp[i] = cur
            result = max(result, dp[i])
        return result
