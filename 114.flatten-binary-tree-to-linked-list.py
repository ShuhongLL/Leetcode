#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            l = root.left
            r = root.right
            l = self.flatten(l)
            r = self.flatten(r)
            root.left = None
            root.right = l
            head = root
            while head.right:
                head = head.right
            head.right = r
            return root
