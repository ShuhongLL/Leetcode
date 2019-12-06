# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root, root)
        
    def dfs(self, n1: TreeNode, n2: TreeNode):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        if n1.val == n2.val:
            return self.dfs(n1.left, n2.right) and self.dfs(n1.right, n2.left)
        return False
