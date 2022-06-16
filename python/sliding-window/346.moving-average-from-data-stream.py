import collections

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.memo = collections.deque([])
        self.size = size
        self.sum = 0
        

    def next(self, val: int) -> float:
        if len(self.memo) >= self.size:
            pre = self.memo.popleft()
            self.sum -= pre
        self.sum += val
        self.memo.append(val)
        return self.sum / len(self.memo)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)