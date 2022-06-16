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
        seen = {}
        queue = [node]
        seen[node] = Node(node.val, [])
        while queue:
            vertex = queue.pop(0)
            for neighbor in vertex.neighbors:
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                seen[vertex].neighbors.append(seen[neighbor])

        return seen[node]
