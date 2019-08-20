#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ''
        nums = list(range(1, n + 1))
        remain = n
        for _ in range(n):
            print(k)
            mod = 1
            for i in range(1, remain):
                mod *= i
            index = k // mod
            remain = k % mod
            k = k - index * mod
            result += str(nums[index])
            del nums[index]
        return result
        