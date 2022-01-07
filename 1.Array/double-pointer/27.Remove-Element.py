class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else:
                start += 1
        return start

# Alternative method: 快慢指针
