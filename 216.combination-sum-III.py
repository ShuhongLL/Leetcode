class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        self.result = set()
        self.k_sum(nums, [], k, n)
        return list(self.result)
        
    def k_sum(self, nums: List[int], path: List[int], k: int, target: int):
        if k == 2:
            seen = {}
            for num in nums:
                if num in seen:
                    self.result.add(tuple(path + [num, seen[num]]))
                elif target - num > 0:
                    seen[target - num] = num
        else:
            for i in range(len(nums)):
                if target - nums[i] > 0:
                    nums_c = nums[:]
                    nums_c.pop(i)
                    self.k_sum(nums_c[i:], path + [nums[i]], k-1, target - nums[i])
