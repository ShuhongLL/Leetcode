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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        self.result = []
        delete = set(to_delete)
        self.dfs(root, delete)
        if root.val not in delete:
            self.result.append(root)
        return self.result
        
    def dfs(self, node: TreeNode, to_delete: set):
        if not node:
            return
        left = node.left
        right = node.right
        if left and left.val in to_delete:
            node.left = None
        if right and right.val in to_delete:
            node.right = None
        if node.val in to_delete:
            if node.left:
                self.result.append(left)
            if node.right:
                self.result.append(right)
        self.dfs(left, to_delete)
        self.dfs(right, to_delete)

# @lc code=end

