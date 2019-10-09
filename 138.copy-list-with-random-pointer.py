#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        deep_clone_dict = {}
        curr = head
        while curr:
            deep_clone_dict[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                deep_clone_dict[curr].next = deep_clone_dict[curr.next]
            if curr.random:
                deep_clone_dict[curr].random = deep_clone_dict[curr.random]
            curr = curr.next
        return deep_clone_dict[head]
# @lc code=end

