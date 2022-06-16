#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
import collections

class TimeMap:
    # binary search
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        return self.binary_search(self.timeMap[key], timestamp)
        
    def binary_search(self, vals: List[tuple], time: int) -> str:
        if not vals:
            return ""
        l, r = 0, len(vals) - 1
        while l < r:
            mid = (l + r)//2
            if vals[mid][1] == time:
                return vals[mid][0]
            if vals[mid][1] < time:
                l = mid + 1
            else:
                r = mid
        if vals[l][1] <= time:
            return vals[l][0]
        if l > 0 and vals[l-1][1] <= time:
            return vals[l-1][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

