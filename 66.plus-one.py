#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        n = -1
        while index >= 0:
            if digits[index] + 1 > 9:
                digits[index] = 0
                n = 1
                index -= 1
            else:
                digits[index] += 1
                return digits
        if n == 1:
            digits.insert(0, 1)
        return digits
