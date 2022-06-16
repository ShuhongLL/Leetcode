class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        fast, slow, prev = 0, 0, 0
        while nums[nums[fast]] in range(0, len(nums)) and nums[nums[nums[fast]]] in range(0, len(nums)):
            fast = nums[nums[nums[fast]]]
            prev = nums[slow]
            slow = nums[nums[slow]]
            if slow == fast:
                break
        else:
            return -1

        p1, p2 = 0, slow
        while p1 != p2:
            p1 = nums[p1]
            prev = p2
            p2 = nums[p2]
        return nums[prev]
