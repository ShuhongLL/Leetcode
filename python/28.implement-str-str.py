#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            return 0

        queryT = self.kmpTable(needle)

        j = 0
        k = 0 
        while j < len(haystack) - 1:
            if haystack[j] == needle[k]:
                j += 1
                k += 1
                if k == len(needle):
                    return j - k
            else:
                k = queryT[k]
                if k < 0:
                    j += 1
                    k = 0

    def kmpTable(self, target: str) -> List[int]:
        nextT = [None] * (len(target) + 1)
        nextT[0] = -1
        pos = 1
        cnd = 0
        while pos < len(target):
            if target[pos] == target[cnd]:
                nextT[pos] = nextT[cnd]
            else:
                nextT[pos] = cnd
                cnd = nextT[cnd]
                while cnd >= 0 and target[pos] != target[cnd]:
                    cnd = nextT[cnd]
                cnd += 1
                pos += 1
        nextT[pos] = cnd

        for x in nextT:
            print(x)
        return nextT
