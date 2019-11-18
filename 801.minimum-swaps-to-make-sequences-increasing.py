#
# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#

# @lc code=start
class Solution:
    def minSwap(self, A: List[int], B: List[int], i: int = 0, count: int = 0) -> int:
        """
        n1: natural count of making i-1 columns increasing and not swapping i-1 th column
        s1: swapped count of making i-1 columns increasing and swapping i-1 th column
        n2: natural count of making i columns increasing and not swapping i th column
        s2: swapped count of making i columns increasing and swapping i th column
        """
        n1, s1 = 0, 1
        for i in range(1, len(A)):
            n2, s2 = float('inf'), float('inf')
            if A[i] > A[i-1] and B[i] > B[i-1]:
                """
                    i-1     i
                A   a1   <  a2 
                B   b1   <  b2
                We don't know if a2 > b1 or b2 > a1
                In order to swap a2 and b2,
                we need a1 and b1 to be swapped, hence s2 = s1 + 1
                """
                n2 = n1
                s2 = s1 + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                """
                    i-1      i
                A   a1   <?  a2     but a2 > b1
                B   b1   <?  b2     but b2 > a1
                We don't know if a2 > a1 or b2 > b1
                In order to keep a2 and b2 unswapped,
                we need a1 and b1 to be swapped, hence n2 = s1 + 1
                """
                n2 = min(n2, s1)
                s2 = min(n1+1, s2)
            n1, s1 = n2, s2
        return min(n2, s2)

# @lc code=end

