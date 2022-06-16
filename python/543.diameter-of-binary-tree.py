#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 1
        self.dfs(root)
        return self.result - 1

    def dfs(self, node: TreeNode):
        if not node:
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.result = max(self.result, l+r+1)
        return max(l, r) + 1
        
# @lc code=end

