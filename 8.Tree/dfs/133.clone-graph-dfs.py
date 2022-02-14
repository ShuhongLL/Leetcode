"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        self.seen = {}
        return self.dfs(node)
        
    def dfs(self, node: 'Node'):
        if node in self.seen:
            return self.seen[node]

        copy = Node(node.val, [])
        self.seen[node] = copy

        if node.neighbors:
            copy.neighbors = [self.dfs(n) for n in node.neighbors]
        return copy