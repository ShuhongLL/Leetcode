#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.row = defaultdict(list)
        self.col = defaultdict(list)
        self.stones = stones
        self.seen_stone = set()
        sum_max = 0
        
        for i in range(len(stones)):
            self.row[stones[i][0]].append(i)
            self.col[stones[i][1]].append(i)

        for i in range(len(stones)):
            if i not in self.seen_stone:
                sum_max += self.dfs(i) - 1
        return sum_max
        
    def dfs(self, index: int):
        if index in self.seen_stone:   return 0
        self.seen_stone.add(index)
        target = list(set(tuple(self.row[self.stones[index][0]] + self.col[self.stones[index][1]])))
        cur_sum = 1
        for i in target:
            cur_sum += self.dfs(i)
        return cur_sum 

# @lc code=end

