#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.results = []
        self.traversal([root], False)
        return self.results

    def traversal(self, nodeList: List[TreeNode], fromRight: bool):
        children = []
        result = []
        for child in nodeList:
            result.append(child.val)
            if child.left != None:
                children.append(child.left)
            if child.right != None:
                children.append(child.right)
        if fromRight:
            result = result[::-1]
        self.results.append(result)
        if len(children) > 0:
            if fromRight:
                self.traversal(children, False)
            else:
                self.traversal(children, True)

