#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        if root.right:
            if root.next and root.next.left:
                root.right.next = root.next.left
            self.connect(root.right)
            if root.left:
                root.left.next = root.right
                self.connect(root.left)
        return root
