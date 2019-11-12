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

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:    return []
        self.to_delete = to_delete
        self.result = []
        self.traversal(root, True)
        return self.result

    def traversal(self, node: TreeNode, isHead: bool):
        if not node:    return
        to_be_head = False
        if node.val not in self.to_delete:
            if isHead:    self.result.append(node)
        else:   to_be_head = True
        if node.left:
            if node.left.val in self.to_delete:
                self.traversal(node.left.left, True)
                self.traversal(node.left.right, True)
                node.left = None
            else:
                self.traversal(node.left, to_be_head)
        if node.right:
            if node.right.val in self.to_delete:
                self.traversal(node.right.left, True)
                self.traversal(node.right.right, True)
                node.right = None
            else:
                self.traversal(node.right, to_be_head)

# @lc code=end

