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
        
    # method 1: stack
        # head_t = ListNode(-1)
        # head_t.next = head
        # curr = head_t
        # count = 0
        # value = []
        # while count != m - 1:
        #     curr = curr.next
        #     count += 1
        # tail = curr.next
        # count += 1
        # while count <= n:
        #     value.append(tail.val)
        #     tail = tail.next
        #     count += 1
        # while value:
        #     curr.next = ListNode(value[-1])
        #     del value[-1]
        #     curr = curr.next
        # curr.next = tail
        # return head_t.next

    # method 2: iterative
        head_t = ListNode(-1)
        head_t.next = head
        prev = head_t
        cur = head
        count = 0

        while count < m - 1:
            cur = cur.next
            prev = prev.next
            count += 1
        tail1 = prev
        head1 = cur

        while count < n:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            count += 1
        head2 = cur
        tail2 = prev
        
        tail1.next = tail2
        head1.next = head2
        return head_t.next


