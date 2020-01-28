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
        if not head:
            return
        self.dfs(head)
        return head

    def dfs(self, root: 'Node'):
        cur = root
        while cur.next:
            if cur.child:
                nxt = cur.next
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
                tail = self.dfs(cur.next)
                tail.next = nxt
                nxt.prev = tail
            cur = cur.next
        # edge case: tail.next = None but tail.child != None
        if cur.child:
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
            return self.dfs(cur.next)
        return cur

# @lc code=end

