import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.result = float('-inf')
        sub = collections.defaultdict(list)
        for i in range(len(manager)):
            sub[manager[i]].append(i)

        def dfs(cur: int, time: int):
            if len(sub[cur]) == 0:
                self.result = max(self.result, time)
            else:
                for emp in sub[cur]:
                    dfs(emp, time+informTime[cur])
                    
        dfs(headID, 0)
        return self.result
