#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return	
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        n = len(nodes)
        middle = n // 2

        for i in range(middle):
            nodes[i].next = nodes[n-1-i]
            nodes[n-1-i].next = nodes[i+1]

        # set the next to be None,
        # otherwise the freaking test will not end
        # and output 'Exceed time limit'
        nodes[middle].next = None
# @lc code=end

