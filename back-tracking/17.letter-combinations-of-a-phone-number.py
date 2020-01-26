#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.result = []
        self.back_tracking(digits, '')
        return self.result
        
    def back_tracking(self, digits: str, path: str):
        num_to_let = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits:
            self.result.append(path)
            return
        for char in num_to_let[digits[0]]:
            self.back_tracking(digits[1:], path + char)
