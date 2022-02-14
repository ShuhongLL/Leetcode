class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        rob, not_rob = 0, 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)
