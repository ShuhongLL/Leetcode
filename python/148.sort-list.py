#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        merge sort
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # split list into two parts in equal length
        f_ptr, b_ptr = head, head
        pre_ptr = head
        while f_ptr and f_ptr.next:
            f_ptr = f_ptr.next.next
            pre_ptr = b_ptr
            b_ptr = b_ptr.next

        # set next to be None to split
        pre_ptr.next = None

        left = self.sortList(b_ptr)
        right = self.sortList(head)

        # merge two sorted lists
        sentinel = ListNode(0)
        cur = sentinel
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        elif right:
            cur.next = right
        return sentinel.next
# @lc code=end

