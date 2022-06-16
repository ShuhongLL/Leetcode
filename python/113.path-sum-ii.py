#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.result = []
        self.findSum(root, sum, [])
        return self.result

    def findSum(self, root:TreeNode, target: int, path: List[int]):
        if root:
            if root.left == None and root.right == None:
                if root.val == target:
                    self.result.append(path + [root.val])
            else:
                self.findSum(root.right, target - root.val, path + [root.val])
                self.findSum(root.left, target - root.val, path + [root.val])

