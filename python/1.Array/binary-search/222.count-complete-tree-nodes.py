#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1:
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0

# Solution 2:
class Solution:
    """
    Binary search in a binary search
    """
    def countNodes(self, root: TreeNode) -> int:
        if not root:    return 0
        depth = self.find_depth(root)
        if depth == 0:  return 1
        
        # another binary search to find out where is the last leaf
        left, right = 0, 2**depth - 1
        while left <= right:
            mid = left + (right - left)//2
            if self.binary_search(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1
        return 2**(depth) - 1 + left
        
    def binary_search(self, index: int,  depth: int, node: TreeNode):
        left, right = 0, 2**depth - 1
        for _ in range(depth):
            mid = left + (right - left)//2
            if index <= mid:
                node = node.left
                right = mid
            elif index > mid:
                node= node.right
                left = mid
        return node is not None
        
    def find_depth(self, node):
        depth = 0
        while node.left:
            node = node.left
            depth += 1
        return depth
# @lc code=end

