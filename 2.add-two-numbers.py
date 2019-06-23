#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry: int = 0) -> ListNode:
        val = l1.val + l2.val + carry
        carry = val // 10
        currNode = ListNode(val % 10)

        if carry != 0 or l1.next or l2.next:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            currNode.next = self.addTwoNumbers(l1.next, l2.next, carry)

        return currNode
