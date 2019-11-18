#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        return self.flattenChild(head)[0]
        
    def flattenChild(self, node: 'Node'):
        cur = tail = node
        while cur:
            nxt = cur.next
            if cur.child:
                h, t = self.flattenChild(cur.child)
                cur.child = None
                cur.next = h
                h.prev = cur
                t.next = nxt
                if nxt: nxt.prev = t
                cur = t
            tail = cur
            cur = nxt
        return node, tail

# @lc code=end

