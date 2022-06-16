class NumArray:
    def __init__(self, nums: List[int]):
        self.memo = nums
        if len(nums) > 1:
            for i in range(1, len(self.memo)):
                self.memo[i] += self.memo[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.memo[j] - self.memo[i-1] if i > 0 else self.memo[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)