#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.recursive(root)
        return self.result

    def recursive(self, root: TreeNode):
        if root:
            self.result.append(root.val)
            self.recursive(root.left)
            self.recursive(root.right)
# @lc code=end

