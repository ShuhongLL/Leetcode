class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start, end = 0, len(nums)-1
        
        def binary_search(start, end, target):
            if start <= end and nums[start] <= target and nums[end] >= target:
                mid = (start + end)//2
                if nums[mid] > target:
                    return binary_search(start, end-1, target)
                elif nums[mid] < target:
                    return binary_search(start+1, end, target)
                else:
                    left_s, _ = binary_search(start, mid-1, target)
                    _, right_e = binary_search(mid+1, end, target)
                    return [left_s if left_s != -1 else mid, right_e if right_e != -1 else mid]
            return [-1, -1]
        
        return binary_search(start, end, target)
