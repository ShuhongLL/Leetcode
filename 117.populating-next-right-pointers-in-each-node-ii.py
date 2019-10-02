#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
import collections

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = collections.deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if i < length - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
