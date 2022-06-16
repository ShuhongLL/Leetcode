# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root)[1]
    
    def dfs(self, node: TreeNode):
        if not node:
            return 0, True
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        return max(l[0], r[0]) + 1, l[1] and r[1] and abs(l[0] - r[0]) < 2
