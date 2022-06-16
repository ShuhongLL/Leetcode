class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        s = [0] * (num+1)
        s[0] = 0
        s[1] = 1
        for i in range(1, num+1):
            count = 0
            while 2 ** (count+1) <= i:
                count += 1
            s[i] = s[i - 2**count] + 1
        return s
