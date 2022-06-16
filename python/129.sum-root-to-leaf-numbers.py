#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum = 0
        self.traversal(root, 0)
        return self.sum

    def traversal(self, root: TreeNode, path: int):
        if root:
            path = path * 10 + root.val
            if not root.left and not root.right:
                self.sum += path
            else:
                self.traversal(root.left, path)
                self.traversal(root.right, path)
# @lc code=end