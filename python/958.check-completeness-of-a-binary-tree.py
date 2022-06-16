#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        self.lists = []
        self.traversal(root, 1)
        return len(self.lists) == max(self.lists)
        
    def traversal(self, node: TreeNode, index: int):
        self.lists.append(index)
        if node.left:
            self.traversal(node.left, index*2)
        if node.right:
            self.traversal(node.right, index*2+1)

# @lc code=end

