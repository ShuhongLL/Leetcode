#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        self.result = []
        return self.divideAndConquer(1, n)

        return self.result
    def divideAndConquer(self, start: int, end: int) -> List[TreeNode]:
        result = []
        if start > end:
            return [None]
        if start == end:
            root = TreeNode(start)
            return [root]
        for i in range(start, end + 1):
            left = self.divideAndConquer(start, i - 1)
            right = self.divideAndConquer(i + 1, end)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)
        return result
        

