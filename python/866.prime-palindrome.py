#
# @lc app=leetcode id=866 lang=python3
#
# [866] Prime Palindrome
#

# @lc code=start
class Solution:
    def primePalindrome(self, N: int) -> int:
        while 1:
            if N == self.reverse(N) and self.isPrime(N):
                return N
            N += 1

            if N != 2 and N % 2 == 0:
                N += 1

            l = len(str(N))
            # all even length palindrome is a mutiple of 11
            # e.g   1221    345543
            if l > 2 and l % 2 == 0:
                N = 10 ** l
        
    def reverse(self, num: int):
        return int(str(num)[::-1])
    
    def isPrime(self, num: int):
        return num > 1 and all(num % n for n in range(2, int(num**.5)+1))

# @lc code=end

