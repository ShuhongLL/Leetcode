#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        # extract sign
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)

        decimal = ''
        seen_remainder = {}
        integer = numerator // denominator
        reminder = numerator % denominator
        while reminder != 0 and reminder not in seen_remainder:
            seen_remainder[reminder] = len(seen_remainder)
            numerator = reminder * 10
            decimal += str(numerator // denominator)
            reminder = numerator % denominator
        if reminder == 0:
            return sign + str(integer) + '.' + decimal
        return sign + str(integer) + '.' + decimal[:seen_remainder[reminder]] + '(' + decimal[seen_remainder[reminder]:] + ')'
# @lc code=end

