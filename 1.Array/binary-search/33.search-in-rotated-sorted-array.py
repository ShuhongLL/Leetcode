class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            # 切点在右边
            # edgecase: start = mid
            # ex: (5,1) find 1
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # 切点在左边
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
