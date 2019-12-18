import itertools

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return [
            "{}:{:0>2d}".format(h,m)
            for h, m in itertools.product(range(12), range(60)) 
            if (bin(h).count('1') + bin(m).count('1'))==num
        ]
