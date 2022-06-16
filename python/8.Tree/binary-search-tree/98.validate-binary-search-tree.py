#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode, above: int = float('-inf'), under: int = float('inf')) -> bool:
        if not root:
            return True
        if root.left and (root.left.val >= root.val or root.left.val <= above):
            return False
        if root.right and (root.right.val <= root.val or root.right.val >= under):
            return False
        return self.isValidBST(root.left, above, root.val) and self.isValidBST(root.right, root.val, under)
