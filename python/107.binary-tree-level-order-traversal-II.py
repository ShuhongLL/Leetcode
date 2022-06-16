# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        self.result = [[]]
        self.bfs(root, 0)
        return reversed(self.result)
        
    def bfs(self, node: TreeNode, depth: int):
        if depth >= len(self.result):
            self.result.append([node.val])
        else:
            self.result[depth].append(node.val)
        if node.left:
            self.bfs(node.left, depth+1)
        if node.right:
            self.bfs(node.right, depth+1)
  