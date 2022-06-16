#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ''
        nums = list(range(1, n + 1))
        mod = 1
        remain = n
        for i in range(1, n + 1):
            mod *= i
        k -= 1
        while nums:
            mod = mod // remain
            target = k // mod
            k = k % mod
            result += str(nums.pop(target))
            remain -= 1
        return result
