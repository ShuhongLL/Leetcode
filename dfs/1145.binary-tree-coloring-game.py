# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.left, self.right = 0, 0
        self.dfs(root, x)
        parent = n - self.left - self.right - 1
        return max(parent, self.left, self.right) > n//2
        
    def dfs(self, node: TreeNode, x: int):
        if not node:
            return 0
        l = self.dfs(node.left, x)
        r = self.dfs(node.right, x)
        if node.val == x:
            self.left = l
            self.right = r
        return l + r + 1
