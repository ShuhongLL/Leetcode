#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # edge
        if not head:
            return None
        if head.next == None:
            return head
        ptr = head
        while ptr.next != None:
            if ptr == head:
                tmp1 = head
                tmp2 = head.next.next
                head = head.next
                head.next = tmp1
                tmp1.next = tmp2
                ptr = tmp1
            else:
                if ptr.next.next == None:
                    break
                tmp1 = ptr.next
                ptr.next = tmp1.next
                tmp2 = ptr.next.next
                ptr.next.next = tmp1
                tmp1.next = tmp2
                ptr = tmp1
        return head
