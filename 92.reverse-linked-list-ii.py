#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        head_t = ListNode(-1)
        head_t.next = head
        curr = head_t
        count = 0
        value = []
        while count != m - 1:
            curr = curr.next
            count += 1
        tail = curr.next
        count += 1
        while count <= n:
            value.append(tail.val)
            tail = tail.next
            count += 1
        while value:
            curr.next = ListNode(value[-1])
            del value[-1]
            curr = curr.next
        curr.next = tail
        return head_t.next


