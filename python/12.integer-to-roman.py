#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        X = ['X', 'C', 'M']
        SX = ['IX', 'XC', 'CM']
        SV = ['IV', 'XL', 'CD']
        V = ['V', 'L', 'D']

        roman = ''
        size = min(3, len(str(num)))
        for i in range(size, 0, -1):
            roman += ''.join([ X[i-1] * (num//(10**i)) ])
            num %= 10**i
            sx = 9 * (10 ** (i-1) )
            v = 5 * (10 ** (i-1) )
            sv = 4 * (10 ** (i-1) )
            if num >= sx:
                roman += SX[i-1]
                num -= sx
            elif num >= v:
                roman += V[i-1]
                num -= v
            elif num >= sv:
                roman += SV[i-1]
                num -= sv
        roman += ''.join([ 'I' * num ])
        return roman
