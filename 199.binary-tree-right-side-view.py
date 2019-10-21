#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.result = {}
        self.left_first_traversal(root, 0)
        return [self.result[key] for key in self.result]

    def left_first_traversal(self, root: TreeNode, depth: int):
        if root:
            self.result[depth] = root.val
            self.left_first_traversal(root.left, depth + 1)
            self.left_first_traversal(root.right, depth + 1)
# @lc code=end

