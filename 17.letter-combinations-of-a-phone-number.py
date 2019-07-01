#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # edge
        if digits == '':
            return []
        
        # create map
        dicts = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        output = []
        #recursive iterate
        def recursiveMap(combination: str, nextDigit: List[str]) -> None:
            if len(nextDigit) == 0:
                output.append(combination)
            else:
                for digit in dicts[nextDigit[0]]:
                    recursiveMap(combination + digit, nextDigit[1:])
        
        recursiveMap('', digits)
        return output
