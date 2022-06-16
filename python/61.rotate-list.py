#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # edge
        if not head:
            return None
        cur = head
        count = 1
        while cur.next:
            cur = cur.next
            count += 1
        k = k % count
        cur.next = head

        cur = head
        for _ in range(count - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        return newHead
