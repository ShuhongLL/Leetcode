#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
class Solution:
    def numDecodings(self, s: str) -> int:
        # edge case
        if not s or (len(s) == 1 and s[0] == '0'):
            return 0
        self.dicts = {}
        self.nums = s
        return self.recursiveFind(0)

    def recursiveFind(self, index: int) -> int:
        if index in self.dicts:
            return self.dicts[index]
        # return 0 if index exceeds the length of chars
        if len(self.nums) == index:
            return 0
        # check if nums[index] is the last char
        if len(self.nums) == index + 1:
            self.dicts[index] = 1
            return 1
        base = int(self.nums[index])
        extra = int(self.nums[index + 1])
        num = base * 10 + extra
        if extra == 0:
            if index + 2 == len(self.nums):
                self.dicts[index] = 1
                return 1
            else:
                val = self.recursiveFind(index + 2)
                self.dicts[index] = val
                return val
        elif num > 26:
            val = self.recursiveFind(index + 1)
            self.dicts[index] = val
            return val
        else:
            if len(self.nums) == index + 2:
                val = 2
                if self.nums[-1] == '0':
                    val = 1
                self.dicts[index] = val
                return val
            else:
                val = self.recursiveFind(index + 1) + self.recursiveFind(index + 2)
                self.dicts[index] = val
                return val
