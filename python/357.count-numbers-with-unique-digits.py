class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        f(0): 1         1
        f(1): 9         10
        f(2): 9*9       91
        f(3): 9*9*8     739
        ...             ...
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        result = 10
        base = cur = 9
        for _ in range(1, n):
            base *= cur
            cur -= 1
            result += base
        return result
 