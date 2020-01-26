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

        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        seen_remainder = {}
        decimal = ''
        integer = numerator // denominator
        remainder = numerator % denominator
        while remainder != 0 and remainder not in seen_remainder:
            seen_remainder[remainder] = len(decimal)
            remainder *= 10
            decimal += str(remainder//denominator)
            remainder = remainder % denominator
        if remainder == 0:
            return f'{sign}{integer}.{decimal}'
        i = seen_remainder[remainder]
        return f'{sign}{integer}.{decimal[:i]}({decimal[i:]})'

# @lc code=end

