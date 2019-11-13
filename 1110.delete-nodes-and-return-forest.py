#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Bottom up + post traversal
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:    return []
        self.to_delete = to_delete
        self.result = []
        if root.val not in self.to_delete:
            self.result.append(root)
        self.traversal(root)
        return self.result

    def traversal(self, node: TreeNode):
        if not node:    return
        self.traversal(node.left)
        self.traversal(node.right)
        
        if node.left and node.left.val in self.to_delete:
            node.left = None
        if node.right and node.right.val in self.to_delete:
            node.right = None
        if node.val in self.to_delete:
            if node.left:   self.result.append(node.left)
            if node.right:  self.result.append(node.right)

# @lc code=end

