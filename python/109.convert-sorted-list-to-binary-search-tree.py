#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nodes = []
        curr = head
        while curr != None:
            nodes.append(curr.val)
            curr = curr.next
        return self.createTree(nodes)
    
    def createTree(self, nodes: List[int]):
        if not nodes:
            return None
        mid = len(nodes) // 2
        root = TreeNode(nodes[mid])
        root.left = self.createTree(nodes[:mid])
        root.right = self.createTree(nodes[mid + 1:])
        return root

