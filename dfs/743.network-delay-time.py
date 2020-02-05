import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        self.graph = collections.defaultdict(list)
        self.memo = {node: float('inf') for node in range(1, N+1)}
        for u, v, w in times:
            self.graph[u].append((w,v))
        self.dfs(K, 0)
        result = max(self.memo.values())
        return result if result != float('inf') else -1
        
    def dfs(self, node, duration):
        # other signal arrived earlier
        if duration >= self.memo[node]:
            return
        self.memo[node] = duration
        for v, w in sorted(self.graph[node]):
            self.dfs(w, v+duration)
