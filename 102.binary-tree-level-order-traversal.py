#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.results = []
        self.traversal([root])
        return self.results

    def traversal(self, nodeList: List[TreeNode]):
        children = []
        result = []
        for child in nodeList:
            result.append(child.val)
            if child.left != None:
                children.append(child.left)
            if child.right != None:
                children.append(child.right)
        self.results.append(result)
        if len(children) > 0:
            self.traversal(children)
