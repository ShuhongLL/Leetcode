import collections

class Solution:
    # solution: bfs
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            cur, depth = queue.popleft()
            if cur == target:
                return depth
            if cur in dead:
                continue
            for nxt in self.find_neighbor(cur):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, depth + 1))
        return -1
        
    def find_neighbor(self, input: str):
        for i in range(4):
            digit = int(input[i])
            for d in [-1, 1]:
                c = (digit + d) % 10
                yield input[:i] + str(c) + input[i+1:]
