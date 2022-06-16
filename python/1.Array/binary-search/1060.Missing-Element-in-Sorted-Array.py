class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # return num of missing at idx
        missing = lambda idx: nums[idx] - nums[0] - idx
        n = len(nums)
        if k > missing(n-1):
            return nums[-1] + k - missing(n-1)
        
        l, r = 0, n-1
        while l < r:
            mid = (l+r)//2
            if missing(mid) < k:
                l = mid + 1
            else:
                r = mid
        # kth missing number is greater than nums[left - 1]
        # and less than nums[left]    
        return nums[l-1] + k - missing(l-1)
