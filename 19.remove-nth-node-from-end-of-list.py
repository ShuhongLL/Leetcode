#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # edge
        if head.next == None or not head:
            return None

        # twp pointer p_1 and p_2
        # p_2 is delayed n steps
        p_1, p_2 = head, head
        while p_1.next != None:
            if n == 0:
                p_2 = p_2.next
            else:
                n -= 1
            p_1 = p_1.next
        # edge cases
        if n == 0:
            p_2.next = p_2.next.next
        else:
            head = head.next
        return head
