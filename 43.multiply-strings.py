#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(num: str) -> int:
            total = 0
            numBuilder = []
            numMap = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
            for i in num:
                numBuilder.append(numMap[i])
            for j in numBuilder:
                total = total*10 + j
            return total
        return str(str_to_int(num1) * str_to_int(num2))
