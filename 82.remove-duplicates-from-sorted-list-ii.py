#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # edge
        if not head:
            return None
        head_t = ListNode(float('-inf'))
        head_t.next = head
        real, prev, curr = head_t, head_t, head

        while curr and curr.next:
            if curr.val != curr.next.val and prev.val != curr.val:
                real.next = curr
                real = real.next
            prev = prev.next
            curr = curr.next

        if curr.val == prev.val:
            real.next = None
        else:
            real.next = curr

        return head_t.next
