#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [(value, timestamp)]
        else:
            self.dict[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        if len(self.dict[key]) == 1:
            return self.dict[key][0][0]
        return self.binary_search(timestamp, self.dict[key])
    

    def binary_search(self, timestamp: int, tree) -> str:
        l, r = 0, len(tree) - 1
        while l + 1 < r:
            mid = l + (r - l)//2
            if tree[mid][1] < timestamp:
                l = mid
            else:
                r = mid - 1
        if tree[r][1] <= timestamp:
            return tree[r][0]
        if tree[l][1] <= timestamp:
            return tree[l][0]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

