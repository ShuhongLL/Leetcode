#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        value = preorder.pop(0)
        node = TreeNode(value)
        index = inorder.index(value)
        node.left = self.buildTree(preorder, inorder[:index])
        node.right = self.buildTree(preorder, inorder[index + 1:])
        return node
