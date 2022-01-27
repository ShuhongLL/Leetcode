class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # sorted input nums
        # memo:
        #   key: the largest value in the subset
        #   value: the subset
        # for each iteration
        # check whether cur num can be divided by each key
        #   if so: select the subset with maximum len + cur num
        #   otherwise: cur num
        memo = {-1: set()}
        for num in sorted(nums):
            memo[num] = max([memo[key] for key in memo if num % key == 0], key = len) | {num}
        return max(memo.values(), key = len)
