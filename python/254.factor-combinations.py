class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.result = set()
        self.back_tracking(n, [])
        return list(self.result)

    def back_tracking(self, value: int, path: List[int]):
        if value == 1 or value == 2:
            return
        for i in range(2, int(value**.5)+1):
            if value % i == 0:
                self.result.add(tuple(sorted(path + [i, value//i])))
                self.back_tracking(value//i, path + [i])
