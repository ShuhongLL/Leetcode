#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = {}
        index = 0
        cur = head
        while cur:
            if cur in seen:
                return cur
            seen[cur] = index
            index += 1
            cur = cur.next
        return None
# @lc code=end

