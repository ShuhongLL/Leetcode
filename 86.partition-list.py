#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # edge
        if not head or head.next == None:
            return head

        t_head = ListNode(-1)
        t_head.next = head
        ptr, split = head, t_head
        while ptr.next != None:
            if ptr.val >= x:
                break
            split = split.next
            ptr = ptr.next
        
        ptr2 = ptr
        tail = ptr
        ptr = ptr.next
        while ptr != None:
            if ptr.val < x:
                split.next = ptr
                tmp = ptr.next
                ptr.next = tail
                split = split.next
                ptr2.next = tmp
                ptr = tmp
            else:
                ptr = ptr.next
                ptr2 = ptr2.next
        return t_head.next

