class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]
        start, end, p = 0, len(nums)-1, len(nums)-1
        while start <= end:
            if nums[start]**2 >= nums[end]**2:
                result[p] = nums[start]**2
                start += 1
            else:
                result[p] = nums[end]**2
                end -= 1
            p -= 1
        return result
# clean: deque, deque.appendleft(), deque.append()
